from api import db
from api.main.data.Note import Note

class NotesRepository:

    def save_note(self, title, body):
        note = Note(title, body)
        db.session.add(note)
        db.session.commit()
        return note

    def get_notes(self):
        return Note.query.all()


    def delete_note(self, id):
        note = Note.query.get(id)
        db.session.delete(note)
        db.session.commit()

# Global Notes Repo... this will go away when persistence is introduced
notesRepo = NotesRepository()
