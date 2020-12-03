from api import db
from api.main.data.Note import Note

class NotesRepository:

    def save_note(self, title, body):
        note = Note(title, body)
        db.session.add(note)
        db.session.commit()
        return note

    def get_note(self, note_id):
        note = Note.query.get(note_id)
        if not note:
            return False
        return note

    def get_notes(self):
        return Note.query.all()

    def delete_note(self, note_id):
        note = Note.query.get(note_id)
        if not note:
            return False
        db.session.delete(note)
        db.session.commit()
        return True

# There's gotta be a better way...
notesRepo = NotesRepository()
