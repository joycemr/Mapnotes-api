from flask_restful import fields

class Note:

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body


resource_fields = {'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,}
