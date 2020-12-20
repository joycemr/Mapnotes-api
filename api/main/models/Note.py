from flask_restful import fields
from sqlalchemy.orm import relationship
from geojson import FeatureCollection
from api import db
from api.main.models.NoteFeature import NoteFeature


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

    def replace_featureCollection(self, featureCollection):
        """ add (or replace) the featureCollection in this object
            each feature in the collection is written to a new NoteFeature
            and added to this notes noteFeatures list
        Args:
            featureCollection (geojson.feature.FeatureCollection): a geoJson list of geometric features
        """
        self.noteFeatures.clear()
        for feature in featureCollection.features:
            noteFeature = NoteFeature(feature, self.id)
            self.noteFeatures.append(noteFeature)

    def get_featureCollection(self):
        """ return a geoJson FeatureCollection
        Returns:
            dict: Python dictionary that represnets a geoJson FeatureCollection
        """
        if len(self.noteFeatures) == 0:
            return {}
        features = []
        for noteFeature in self.noteFeatures:
            features.append(noteFeature.get_feature())
        return FeatureCollection(features)
