from flask import Flask

from routes import api

app = Flask(__name__)
# limits max file upload size to 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

# api = Api(app) # Api() replaced by ./routes/__init__.py
api.init_app(app)

if __name__ == '__main__':
  app.run(debug=True)