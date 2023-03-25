# Social_Flask
Social Flask is a social media platform built using Flask, a Python web framework. The platform allows users to create an account,create/write post, view the date of post created.

## Getting Started
### Prerequisites
Before running the application, ensure that you have the following installed on your machine:
- Python 3.8 or higher
- Flask 2.2 or higher
- Flask SQLAlchemy 3.0 or higher

### Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/sdivyanshu90/Social_Flask.git
```

2. Navigate to the project directory:
```
cd Social_Flask
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Set the Flask app environment variable:
```
export FLASK_APP=app.py
```

2. Run the application:
```
flask run
```

3. Access the application in your web browser:
```
http://localhost:5000
http://127.0.0.1:5000
```

*Note*: If port 5000 is already in use, you can free the port by running fuser -k port/tcp command in the terminal.
Also, to quit or stop the server, press Ctrl+C because Ctrl+Z sends the process to the background.

## Features
- User registration and authentication
- User profile creation and editing
- Post creation and editing

## Contributing
Contributions are welcome! Please submit a pull request with your changes.

