from flask_restful import fields
from sqlalchemy.orm import relationship
from api import db

class Note(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer, db.Sequence('note_seq'), primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    noteFeatures = relationship("NoteFeature", back_populates="note", cascade="all, delete-orphan")

    def __init__(self, title, body, **kwargs):
        self.title = title
        self.body = body

    def __str__(self):
        return 'Note_id: {} Title: {} Body: {} Features: {}'.format(self.id, self.title, self.body, self.get_featureCollection())

    def get_featureCollection(self):
        if len(self.noteFeatures) == 0:
            return {}
        collection = {"type": "FeatureCollection", "features": []}
        for noteFeature in self.noteFeatures:
            collection['features'].append(noteFeature.get_feature())
        return collection


resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,}
