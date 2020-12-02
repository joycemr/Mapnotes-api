# This has to be at the top to prevent the cache directories
import sys
sys.dont_write_bytecode = True

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from main.controllers.MapnotesController import MapnotesController

app = Flask(__name__)
api = Api(app)

api.add_resource(MapnotesController, '/notes', '/notes/<int:note_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
