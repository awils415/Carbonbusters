from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_Name = db.Column(db.String(150))
    last_Name = db.Column(db.String(150))
    co2emissions = db.Column(db.Integer)
    trees = db.Column(db.Integer)
    one_year = db.Column(db.Integer)
    two_years = db.Column(db.Integer)
    three_years = db.Column(db.Integer)
    ten_dollar = db.Column(db.Integer)