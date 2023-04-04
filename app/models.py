from datetime import datetime

from app import db


# class Categories(db.Model):
#     category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     category_name = db.Column(db.String(32), nullable=False)
#     tasks = db.relationship('Tasks', backref='category', lazy='dynamic')


class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(64))
    # category = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    category = db.Column(db.String(32), nullable= False)
    added_at = db.Column(db.DateTime, default=datetime.now())
    deadline = db.Column(db.Date)
    is_urgent = db.Column(db.Integer, default=5)
    is_done = db.Column(db.Boolean, default=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_tasks(cls):
        return cls.query.all()

    @classmethod
    def set_task_as_complete(cls,task_id):
        Tasks.query.get(task_id).is_done = True
        db.session.commit()

    def __str__(self):
        return self.description


# class Users(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(64), unique=True)
#     password = db.Column(db.String(64), nullable=False)
