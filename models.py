from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Show(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    songs = db.relationship('Song', backref='show', lazy=True)


class Song(db.Model):
    title = db.Column(db.String(100), nullable=False, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)

    def __repr__(self):
        return self.title

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(100), db.ForeignKey('song.title'), nullable=False)
    dancer = db.Column(db.String(100), nullable=False)

    song = db.relationship('Song', backref='performances', lazy=True)

    def __repr__(self):
        return f"<Performance {self.dancer}>"