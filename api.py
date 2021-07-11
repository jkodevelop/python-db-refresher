from util.config import config

from flask import Flask
from flask_jwt_extended import JWTManager

from routes import api

app = Flask(__name__)

# limits max file upload size
app.config['MAX_CONTENT_LENGTH'] = config['FLASK.default']['MAX_CONTENT_LENGTH']
# print(f'::{app.config["MAX_CONTENT_LENGTH"]}::')

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = config['FLASK.default']['JWT_SECRET_KEY']
# print(f'::{app.config["JWT_SECRET_KEY"]}::')

jwt = JWTManager(app)

# api = Api(app) # Api() replaced by ./routes/__init__.py
api.init_app(app)

if __name__ == '__main__':
  app.run(debug=True, threaded=True)