from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    carrer_points = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    players = db.relationship('Player', backref = 'team')