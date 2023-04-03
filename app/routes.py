import flask

from app import flask_app
from .forms import AddTodo


@flask_app.route('/')
def home():
    form = AddTodo()
    return flask.render_template('index.html', form=form)
