# This has to be at the top to prevent the cache directories
import sys
sys.dont_write_bytecode = True

from api import app, api

from api.main.controllers.Notes import NotesList
from api.main.controllers.Notes import Notes
from api.main.controllers.Features import Features
api.add_resource(NotesList, '/notes')
api.add_resource(Notes, '/notes/<int:note_id>')
api.add_resource(Features, '/notes/<int:note_id>/features')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
