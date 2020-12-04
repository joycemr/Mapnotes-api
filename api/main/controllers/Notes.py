from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from api.main.repositories.NotesRepository import notesRepo
from api.main.data.Note import resource_fields


class Notes(Resource):

    @marshal_with(resource_fields)
    def get(self, note_id):
        note = notesRepo.get_note(note_id)
        if not note:
            abort(404, message="Mapnote id={} doesn't exist".format(note_id))
        return note

    def delete(self, note_id):
        del_bool = notesRepo.delete_note(note_id)
        if not del_bool:
            abort(404, message="Mapnote id={} doesn't exist".format(note_id))
        return '', 204