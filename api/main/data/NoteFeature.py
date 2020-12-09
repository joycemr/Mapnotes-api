from typing import Sequence
from flask_restful import fields
from api import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry


class NoteFeature(db.Model):

	__tablename__ = 'note_features'

	id = db.Column(db.Integer, db.Sequence('note_features_surrogate_seq'), primary_key=True)
	geometry = db.Column(Geometry(srid=4326))
	notes_id = db.Column(db.Integer, ForeignKey('notes.id'))

	note = relationship("Note", back_populates="noteFeatures")

	def __init__(self, geometry, notes_id, **kwargs):
		self.geometry = geometry
		self.notes_id = notes_id

	def __str__(self):
		return 'Note_id: {} Feature_id: {} Geometry'.format(self.notes_id, self.id, self.geometry)
