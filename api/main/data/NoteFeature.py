from typing import Sequence
from api import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from shapely.geometry import shape
from geoalchemy2.shape import from_shape
import json

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
		return 'Note_id: {} Feature_id: {} Geometry'.format(self.notes_id, self.id, self.geometry)

	# My Conversion
	# I made this work by experimentation, but I'll probably stick with the shapely package
	# just wanted to keep this for posterity
	def geojson_feature_to_wkt_geom(self, geojson_feature):
		wkt_geometry = {"type": "Polygon", "coordinates": geojson_feature['geometry']['coordinates']}
		return json.dumps(wkt_geometry)

	def geojson_feature_to_WKBElement(self, geojson_feature):
		""" convert a geojson geometry feature to a WKBElement
		Args:
			geojson_feature (geojson): a feature in geojson
		Returns:
			geoalchemy2.elements.WKBElement: in GEOAlchemy this wraps a WKB value
		"""
		return from_shape(shape(geojson_feature['geometry']))
