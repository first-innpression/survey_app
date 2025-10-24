
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()

class Result(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), nullable = False)
    favorite_time = db.Column(db.String(50), nullable = False)
    favorite_season = db.Column(db.String(50), nullable = False)
    favorite_actor = db.Column(db.String(50), nullable = False)
    favorite_genres =db.Column(db.String(50), nullable = False)
