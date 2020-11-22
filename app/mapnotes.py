from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)

class Note:

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
}

class NotesRepository:

    id_seq = 0
    notes_dict = {}

    def get_next_id(self):
        self.id_seq = self.id_seq + 1
        return self.id_seq

    def save_note(self, title, body):
        id = self.get_next_id()
        note = Note(id, title, body)
        self.notes_dict[id] = note
        return self.notes_dict[id]

    def delete_note(self, id):
        self.notes_dict.pop(id)

notesRepo = NotesRepository()
class MapnotesController(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('body', type=str)

    @marshal_with(resource_fields)
    def get(self):
        retList = []
        for note in notesRepo.notes_dict.items():
            retList.append(note[1])
        return retList

    @marshal_with(resource_fields)
    def post(self):
        args = self.parser.parse_args()
        newNote = notesRepo.save_note(args['title'], args['body'])
        return newNote, 201

class MapnoteController(Resource):

    def delete(self, note_id):
        self.abort_if_todo_doesnt_exist(note_id)
        notesRepo.delete_note(note_id)
        return '', 204

    def abort_if_todo_doesnt_exist(self, note_id):
        if note_id not in notesRepo.notes_dict:
            abort(404, message="Mapnote {} doesn't exist".format(note_id))


api.add_resource(MapnotesController, '/notes')
api.add_resource(MapnoteController, '/notes/<int:note_id>')

if __name__ == '__main__':
    app.run(debug=True)
