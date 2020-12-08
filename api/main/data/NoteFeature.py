from typing import Sequence
from flask_restful import fields
from api import db
from geoalchemy2 import Geometry


class NoteFeature(db.Model):

	__tablename__ = 'note_features'

	id = db.Column(db.Integer, db.Sequence('note_features_surrogate_seq'), primary_key=True)
	geometry = (Geometry)
	notes_id = db.Column(db.Integer)

	def __init__(self, geometry, notes_id, **kwargs):
		self.geometry = geometry
		self.notes_id = notes_id

