# This has to be at the top to prevent the cache directories
import sys
sys.dont_write_bytecode = True

from api import app, api

from api.main.controllers.Notes import NotesList
from api.main.controllers.Notes import Notes
api.add_resource(NotesList, '/notes')
api.add_resource(Notes, '/notes/<int:note_id>')

if __name__ == '__main__':
    app.run(debug=True)
