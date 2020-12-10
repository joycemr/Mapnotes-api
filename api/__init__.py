from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

db_host = getenv('DB_HOST')
db_user = getenv('DB_USER')
db_password = getenv('DB_PASSWORD')
db_name = getenv('DB_NAME')
db_port = getenv('DB_PORT')

db_uri = 'postgresql://' + db_user + ':' + db_password + '@' + db_host + '/' + db_name

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
api = Api(app)

from api.main.repositories.NotesRepository import NotesRepository
notesRepo = NotesRepository()
