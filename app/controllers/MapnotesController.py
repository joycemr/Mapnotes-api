from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from repositories.NotesRepository import notesRepo
from data.Note import resource_fields, parser


class MapnotesController(Resource):

    @marshal_with(resource_fields)
    def get(self):
        retList = []
        for note in notesRepo.notes_dict.items():
            retList.append(note[1])
        return retList

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        newNote = notesRepo.save_note(args['title'], args['body'])
        return newNote, 201
