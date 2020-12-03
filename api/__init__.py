from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mapnotes_api_user:password@localhost/mapnotes_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

