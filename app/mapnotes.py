# This has to be at the top to prevent the cache directories
import sys
sys.dont_write_bytecode = True

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from controllers.MapnoteController import MapnoteController
from controllers.MapnotesController import MapnotesController

app = Flask(__name__)
api = Api(app)

api.add_resource(MapnotesController, '/notes')
api.add_resource(MapnoteController, '/notes/<int:note_id>')

if __name__ == '__main__':
    app.run(debug=True)
