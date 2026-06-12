
from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Place =  db.Column(db.String(1000) , nullable = False)
    Lattitude = db.Column(db.String(1000) , nullable = False)
    Longitude = db.Column(db.String(1000) , nullable = False)
    Address = db.Column(db.String(5000) , nullable = False)
    place_id = db.Column(db.String(1000) , nullable = False) 

    def __repr__(self):
        return f'Location last searched Succesfuly\n{self.Place}\n{self.Lattitude}\n{self.Longitude}\n{self.Address}\n{self.place_id}'

    
