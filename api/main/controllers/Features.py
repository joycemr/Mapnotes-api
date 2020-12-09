from flask_restful import Resource, abort
from flask import request, jsonify
from api.main.data.Note import resource_fields
from geojson import FeatureCollection
from api.main.data.NoteFeature import NoteFeature
from api.main.data.Note import Note
from api.main.repositories.NotesRepository import notesRepo


class Features(Resource):

    def get(self, note_id):
        return '{"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[-7485586.996581525,-226235.48735737102],[-6305296.5676016435,-2244564.1766917016],[-8932993.786875354,-1147342.2853650213],[-8648270.63382734,78293.21631647227],[-7485586.996581525,-226235.48735737102]]]},"properties":null}]}', 200

    def put(self, note_id):
        featureCollection = FeatureCollection(request.json)
        note = notesRepo.get_note(note_id)
        if not note:
            abort(404, message="Mapnote id={} doesn't exist".format(note_id))
        for feature in featureCollection.features:
            note.add_feature(feature)
        print(note.features)
        return jsonify(featureCollection)

