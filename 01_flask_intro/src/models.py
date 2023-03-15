from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    pets = db.relationship('Pet', backref='owner')
    
    def __repr__(self):
        return f"""
        <Owner, first_name: {self.first_name}
                last_name" {self.last_name}> """
    
    def to_dict(self):
        return {'Id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name}

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f"""
        <Pet, name: {self.name}, species: {self.species}"""
    
    def to_dict(self):
        return {'Id': self.id,
                'Name': self.name,
                'Species': self.species}