from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful_swagger_3 import Api
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
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)
api = Api(app,
	swagger_prefix_url='/notes/doc',
	contact={'name':'Micheal Joyce',
		'email':'michael.joyce@illiniarts.com'
	},
	description = {'title': 'MapNotes',
		'description': 'api to save and retrieve the text and geographic portions of map notes',
		'version': '1.0'
	}
)

from api.main.repositories.NotesRepository import NotesRepository
notesRepo = NotesRepository()
