from flask_restful import Resource, abort
from flask import request, jsonify
from api.main.data.Note import resource_fields
from geojson import FeatureCollection
from api.main.data.NoteFeature import NoteFeature
from api.main.data.Note import Note
from api.main.repositories.NotesRepository import notesRepo
from api import db


class Features(Resource):

    def get(self, note_id):
        return '', 200

    def put(self, note_id):
        featureCollection = FeatureCollection(request.json)
        note = notesRepo.get_note(note_id)
        if not note:
            abort(404, message="Mapnote id={} doesn't exist".format(note_id))
        note.noteFeatures.clear()
        for feature in featureCollection.features:
            noteFeature = NoteFeature(feature, note_id)
            note.noteFeatures.append(noteFeature)
        notesRepo.save_note(note)
        return 'FeatureCollection added', 201

