import flask

from app import flask_app


@flask_app.route('/')
def home():
    return 'home page'
