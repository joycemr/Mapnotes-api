from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from repositories.NotesRepository import notesRepo

class MapnoteController(Resource):

    def delete(self, note_id):
        self.abort_if_todo_does_not_exist(note_id)
        notesRepo.delete_note(note_id)
        return '', 204

    def abort_if_todo_does_not_exist(self, note_id):
        if note_id not in notesRepo.notes_dict:
            abort(404, message="Mapnote {} doesn't exist".format(note_id))
