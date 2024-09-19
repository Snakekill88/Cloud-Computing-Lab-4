from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dominic!'

@app.route('/<name>')
def show_name(name):
    # show the user profile for that user
    return f'Hello {escape(username)}'
