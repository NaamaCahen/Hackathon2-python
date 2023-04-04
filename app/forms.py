import datetime

import flask_wtf
import wtforms


def validate_deadline(form, field):
    if field.data < datetime.date.today():
        raise wtforms.ValidationError('you chose a past time for the deadline. please choose a future date!')


class AddTodo(flask_wtf.FlaskForm):
    description = wtforms.StringField("add a task", [wtforms.validators.DataRequired()], )
    category = wtforms.StringField('category', [wtforms.validators.DataRequired()])
    deadline = wtforms.DateField('deadline',
                                 validators=[validate_deadline])  # add validator to check it is a future date
    is_urgent = wtforms.IntegerField('is urgent')  # add validator to limit the number between 0 and 10
    add_button = wtforms.SubmitField('add')
