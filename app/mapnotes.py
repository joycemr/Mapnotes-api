from flask import Flask, request
from flask_restful import Resource, Api, marshal
import json

app = Flask(__name__)
api = Api(app)

class Note:

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body


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
        return self.notes_dict[1]


class MapnotesController(Resource):

    notesRepo = NotesRepository()

    def get(self):
        return json.dumps(self.notesRepo.__dict__)

    def put(self):
        newNote = self.notesRepo.save_note(request.form['title'], request.form['body'])
        return json.dumps(newNote.__dict__)


api.add_resource(MapnotesController, '/notes')

if __name__ == '__main__':
    app.run(debug=True)
