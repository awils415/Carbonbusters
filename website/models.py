from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Offset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trees = db.Column(db.Integer)
    money = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id '))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_Name = db.Column(db.String(150))
    last_Name = db.Column(db.String(150))
    co2emissions = db.Column(db.Integer)
    offsets = db.relationship('Offset')