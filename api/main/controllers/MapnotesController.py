from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from api.main.repositories.NotesRepository import notesRepo
from api.main.data.Note import resource_fields


class MapnotesController(Resource):

    @marshal_with(resource_fields)
    def get(self):
        # retList = []
        # for note in notesRepo.notes_dict.items():
        #     retList.append(note[1])
        return notesRepo.get_notes()

    @marshal_with(resource_fields)
    def post(self):
        args = self.parser.parse_args()
        if not args['title']:
            abort(400, message="Mapnote must have a non-null title")
        newNote = notesRepo.save_note(args['title'], args['body'])
        return newNote, 201

    def delete(self, note_id):
        self.abort_if_todo_does_not_exist(note_id)
        notesRepo.delete_note(note_id)
        return '', 204

    def abort_if_todo_does_not_exist(self, note_id):
        if note_id not in notesRepo.notes_dict:
            abort(404, message="Mapnote {} doesn't exist".format(note_id))


    # Incoming argument parser
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('body', type=str)