import flask_wtf
import wtforms


class AddTodo(flask_wtf.FlaskForm):
    add_task_input = wtforms.StringField("add a task", [wtforms.validators.DataRequired()])
    add_button = wtforms.SubmitField('add')
