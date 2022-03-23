from app import app
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(64))
   

class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(6), unique = True)
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))