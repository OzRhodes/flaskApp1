from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    # Define the schema
    id = db.Column(db.Integer, primary_key = True)  #primary key
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(50))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key association/relation
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # one to many 
    notes = db.relationship('Note')


