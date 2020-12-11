from marshmallow import Schema, fields

class NoteOutgoing(Schema):
    id = fields.Integer()
    title = fields.Str()
    body = fields.Str()
