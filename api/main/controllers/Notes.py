from flask_restful import Resource, abort, reqparse
from flask_apispec import marshal_with
from api import notesRepo
from api.main.models.Note import Note
from api.dto.NoteOutgoing import NoteOutgoing


class NotesList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('body', type=str)

    @marshal_with(NoteOutgoing(many=True))
    def get(self):
        return notesRepo.get_notes()

    @marshal_with(NoteOutgoing)
    def post(self):
        args = self.parser.parse_args()
        if not args['title']:
            abort(400, message="Mapnote must have a non-null title")
        newNote = Note(args['title'], args['body'])
        return notesRepo.save_note(newNote), 201


class Notes(Resource):

    @marshal_with(NoteOutgoing)
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
