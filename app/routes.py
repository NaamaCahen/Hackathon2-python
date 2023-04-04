import flask

from app import flask_app, db
from .forms import AddTodo
from .models import Tasks


@flask_app.route('/', methods=('GET', 'POST'))
def home():
    form = AddTodo()
    if form.validate_on_submit():
        new_task = Tasks(description=form.description.data, category=form.category.data, deadline=form.deadline.data,
                         is_urgent=form.is_urgent.data)
        new_task.save_task_to_db()
        return flask.redirect('/')
    tasks = Tasks.get_todo_tasks()
    return flask.render_template('index.html', form=form, tasks=tasks)


@flask_app.route('/complete/<int:task_id>')
def complete(task_id):
    Tasks.set_task_as_complete(task_id)
    return flask.redirect('/')


@flask_app.route('/delete/<int:task_id>')
def delete_task(task_id):
    Tasks.delete_task(task_id)
    return flask.redirect('/')


@flask_app.route('/clear-all')
def clear_all_tasks():
    db.session.query(Tasks).delete()
    db.session.commit()
    return flask.redirect('/')


@flask_app.route('/done-tasks')
def show_done_tasks():
    tasks = Tasks.get_done_tasks()
    return flask.render_template('done.html', tasks=tasks)


@flask_app.route('/order-by-urgency')
def order_by_urgency():
    tasks = Tasks.get_todo_tasks().order_by(Tasks.is_urgent.desc())
    return flask.render_template('orderby.html', tasks=tasks, order='urgency')
