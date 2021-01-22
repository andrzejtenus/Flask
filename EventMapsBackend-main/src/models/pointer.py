import datetime
from src import db


class Pointer(db.Model):

    __tablename__ = "pointers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    likes = db.Column(db.Integer, nullable=False)

    def __init__(self, description, longitude, latitude, created_by):
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.created_on = datetime.datetime.now()
        self.created_by = created_by
        self.likes = 0

    def get_id(self):
        return self.id

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'description': self.description,
           'longitude'  : self.longitude,
           'latitude'   : self.latitude,
           'created_on' : self.created_on,
           'created_by' : self.created_by,
           'likes'      : self.likes
       }