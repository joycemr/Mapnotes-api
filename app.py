# This has to be at the top to prevent the cache directories
import sys
sys.dont_write_bytecode = True

from api import app, api

from api.main.controllers.MapnotesController import MapnotesController
from api.main.controllers.MapnoteController import MapnoteController
api.add_resource(MapnotesController, '/notes')
api.add_resource(MapnoteController, '/notes/<int:note_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
