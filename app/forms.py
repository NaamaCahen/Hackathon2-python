from datetime import datetime

import flask_wtf
import wtforms


class AddTodo(flask_wtf.FlaskForm):
    description = wtforms.StringField("add a task", [wtforms.validators.DataRequired()],)
    category = wtforms.StringField('category',[wtforms.validators.DataRequired()])
    deadline = wtforms.DateField('deadline') #add validator to check it is a future date
    is_urgent = wtforms.IntegerField('is urgent') #add validator to limit the number between 0 and 10
    add_button = wtforms.SubmitField('add')

    # def validate_deadline(self, deadline):
    #     if deadline.data < datetime.now():
    #         raise wtforms.ValidationError('you chose a past time for the deadline. please choose a future date!')

