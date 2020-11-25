from flask_restful import fields, reqparse

class Note:

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body


resource_fields = {'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,}

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('body', type=str)