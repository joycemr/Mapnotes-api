from typing import Sequence
from flask_restful import fields
from api import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from shapely.geometry import shape
import json


class NoteFeature(db.Model):

	__tablename__ = 'note_features'

	id = db.Column(db.Integer, db.Sequence('note_features_surrogate_seq'), primary_key=True)
	geometry = db.Column(Geometry(srid=4326))
	notes_id = db.Column(db.Integer, ForeignKey('notes.id'))

	note = relationship("Note", back_populates="noteFeatures")

	def __init__(self, feature, notes_id, **kwargs):
		wkt_geometry = {"type": "Polygon", "coordinates": feature['geometry']['coordinates']}
		self.geometry = json.dumps(wkt_geometry)
		# self.geometry = 'POLYGON((-71.1776585052917 42.3902909739571,-71.1776820268866 42.3903701743239, -71.1776063012595 42.3903825660754,-71.1775826583081 42.3903033653531,-71.1776585052917 42.3902909739571))'
		self.notes_id = notes_id

	def __str__(self):
		return 'Note_id: {} Feature_id: {} Geometry'.format(self.notes_id, self.id, self.geometry)
