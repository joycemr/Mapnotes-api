from api import db
from api.main.data.Note import Note

class NotesRepository:

    def save_note(self, note):
        """ save an existing Note
        Args:
            Note (Note): a map note
        Returns:
            boolean: True if okay, False if not
        """
        db.session.add(note)
        db.session.commit()
        return note

    def get_note(self, note_id):
        """ return a Note
        Args:
            note_id (Integer): Note.id
        Returns:
            Note: map note
        """
        note = Note.query.get(note_id)
        if not note:
            return False
        return note

    def get_notes(self):
        """ get a list of all notes
        Returns:
            [Note]: list of all notes
        """
        return Note.query.all()

    def delete_note(self, note_id):
        """ delete one note
        Args:
            note_id (Integer): note.id
        Returns:
            boolean: True if note found, False if not
        """
        note = Note.query.get(note_id)
        if not note:
            return False
        db.session.delete(note)
        db.session.commit()
        return True
