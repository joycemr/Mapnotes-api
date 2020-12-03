from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from api.main.repositories.NotesRepository import notesRepo
from api.main.data.Note import resource_fields


class MapnotesController(Resource):

    @marshal_with(resource_fields)
    def get(self):
        return notesRepo.get_notes()

    @marshal_with(resource_fields)
    def post(self):
        args = self.parser.parse_args()
        if not args['title']:
            abort(400, message="Mapnote must have a non-null title")
        newNote = notesRepo.save_note(args['title'], args['body'])
        return newNote, 201



    # Incoming argument parser
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('body', type=str)