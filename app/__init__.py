import flask_sqlalchemy
import flask_migrate
from flask import Flask

flask_app = Flask(__name__)

db_info = {'host': 'topsy.db.elephantsql.com',
           'database': 'xwskhzac',
           'psw': 'Q6XzMyT9As_1k5E-Zs-kJnOLuo3MX2XG',
           'user': 'xwskhzac',
           'port': ''}

flask_app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import routes, models
