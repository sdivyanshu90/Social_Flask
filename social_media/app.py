from flask import Flask, render_template, redirect, request, url_for, session,abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
# from auth import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)





class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Account %r>' % self.id

class FoodPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    creator = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<FoodPost %r>' % self.id

@app.route('/', methods=['GET', 'POST'])
def index():
    # If user submits form
    if request.method == "POST":
        # Get response and user's Account object from db
        # if query does not return None aka user is in database
        # Check if response's password is the same as the user's password
        # If it is, redirect to homepage
        # Else if not, return an "invalid password" error

        form = request.form # User Response
        user = Account.query.filter_by(email=str(request.form['email'])).first() # Query for user

        if user is not None: # Validating query
            if str(form['password']) == user.password: # Checking password
                return redirect(f'/home/{user.id}/{user.password}')
            else:
                return "Invalid password"
        else:
            return "Invalid email or password"
    else:
        return render_template('index.html')

@app.route('/createaccount', methods=['GET', 'POST'])
def create_account():
    # If user submits form
    if request.method == "POST":
        # Check if response's username already exists
        # If email has "@" in it and the user's email is not already in use
        # Create a new Account object for user
        # Commit to Database
        user_exists = Account.query.filter_by(email=str(request.form['email'])).first() # Query for user with same email

        if "@" in str(request.form['email']) and user_exists is None: # Checking account existance and email validity

            # Commiting to Database
            new_account = Account(email=request.form['email'], username=request.form['username'], password=request.form['password'])

            try:
                db.session.add(new_account)
                db.session.commit()
                return redirect('/')
            except:
                return "There was an issue while creating your account, please try again later D:"
        else:
            return "Invalid email or that account already exists."
    # If not post request has been sent, return regular html page
    else:
        return render_template('create_account.html')


@app.route('/home/<int:id>/<string:password>', methods=['GET', 'POST'])
def home(id, password):
    # If the client clicks on create new post, redirect client to create_post page
    # Else, return the default home_page.html template
    response = request.form
    if request.method == "POST":
        return redirect(f"/create_post/{id}/{password}")
    else:
        return render_template("home_page.html", posts=FoodPost.query.all(), id=id, password=password)


@app.route('/create_post/<int:id>/<string:password>', methods=['GET', 'POST'])
def create_post(id, password):
    if request.method == "POST":
        response = request.form
        new_post = FoodPost(title=response['title'], content=response['content'], creator=Account.query.filter_by(id=id).first().username)

        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect(f"/home/{id}/{password}")
        except:
            return "There was an issue processing your post, please try again later :("
    else:
        return render_template("new_post.html", id=id, password=password)

@app.route('/view_post/<int:user_id>/<string:password>/<int:post_id>', methods=['GET', 'POST'])
def view_post(user_id, password, post_id):
    post = FoodPost.query.filter_by(id=post_id).first()
    if request.method == "POST":
        return redirect(f"/home/{user_id}/{password}")
    else:
        return render_template('view_post.html', user_id=user_id, password=password, post=post)



if __name__ == "__main__":
    app.run(debug=True)