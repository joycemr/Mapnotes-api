from flask_restful import fields
from api import db

class Note(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body


resource_fields = {'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,}
