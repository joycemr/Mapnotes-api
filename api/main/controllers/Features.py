from flask import request
from flask_restful import Resource, abort
from geojson import FeatureCollection
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
        note.replace_featureCollection(FeatureCollection(request.json))
        notesRepo.save_note(note)
        return 'FeatureCollection added', 201
