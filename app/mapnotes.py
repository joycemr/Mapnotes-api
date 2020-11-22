from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with

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
    # 'uri': fields.Url('todo_ep')
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

class MapnotesController(Resource):

    notesRepo = NotesRepository()

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('body', type=str)

    @marshal_with(resource_fields)
    def get(self):
        retList = []
        for note in self.notesRepo.notes_dict.items():
            retList.append(note[1])
        return retList

    @marshal_with(resource_fields)
    def post(self):
        args = self.parser.parse_args()
        newNote = self.notesRepo.save_note(args['title'], args['body'])
        return newNote


api.add_resource(MapnotesController, '/notes')

if __name__ == '__main__':
    app.run(debug=True)
