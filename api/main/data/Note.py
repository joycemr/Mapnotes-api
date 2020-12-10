from typing import Sequence
from sqlalchemy.orm import backref, relationship
from flask_restful import fields
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
        return 'Note_id: {} Title: {} Body: {} Features: {}'.format(self.id, self.title, self.body, self.noteFeatures)

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,}
