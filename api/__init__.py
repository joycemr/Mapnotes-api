from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app, origins="*")

### Swagger ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "MapNotes api"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

### postgreSQL DB ###
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

api = Api(app)

from api.main.repositories.NotesRepository import NotesRepository
notesRepo = NotesRepository()
