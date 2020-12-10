from flask import request
from flask_restful import Resource, abort
from geojson import FeatureCollection
from api.main.data.NoteFeature import NoteFeature
from api.main.data.Note import Note
from api.main.repositories.NotesRepository import notesRepo


class Features(Resource):

    def get(self, note_id):
        note = notesRepo.get_note(note_id)
        if not note:
            abort(404, message="Mapnote id={} doesn't exist".format(note_id))
        return note.get_featureCollection(), 200

    def put(self, note_id):
        note = notesRepo.get_note(note_id)
        if not note:
            abort(404, message="Mapnote id={} doesn't exist".format(note_id))
        note.noteFeatures.clear()
        featureCollection = FeatureCollection(request.json)
        for feature in featureCollection.features:
            noteFeature = NoteFeature(feature, note_id)
            note.noteFeatures.append(noteFeature)
        notesRepo.save_note(note)
        return 'FeatureCollection added', 201

