from data.Note import Note

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

# Global Notes Repo... this will go away when persistence is introduced
notesRepo = NotesRepository()
