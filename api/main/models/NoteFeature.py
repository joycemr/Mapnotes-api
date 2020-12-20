from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import shape
from geojson import Feature
from api import db

class NoteFeature(db.Model):

	__tablename__ = 'note_features'

	id = db.Column(db.Integer, db.Sequence('note_features_surrogate_seq'), primary_key=True)
	geometry = db.Column(Geometry(srid=4326))
	notes_id = db.Column(db.Integer, ForeignKey('notes.id'))

	note = relationship("Note", back_populates="noteFeatures")

	def __init__(self, feature, notes_id, **kwargs):
		self.geometry = self.geojson_feature_to_WKBElement(feature)
		self.notes_id = notes_id

	def __str__(self):
		return 'Note_id: {} Feature_id: {} Geometry'.format(self.notes_id, self.id, self.get_feature())

	def geojson_feature_to_WKBElement(self, feature):
		""" convert a geojson geometry feature to a WKBElement
		Args:
			geojson_feature (geojson): a feature in geojson
		Returns:
			geoalchemy2.elements.WKBElement: in GEOAlchemy this wraps a WKB value
		"""
		return from_shape(shape(feature['geometry']))

	def get_feature(self):
		""" Return the Feature object
		Returns:
			geojson.Feature: a geojson Feature
		"""
		return Feature(geometry=to_shape(self.geometry), properties=None)
