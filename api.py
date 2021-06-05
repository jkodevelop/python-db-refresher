from flask import Flask

from routes import api

app = Flask(__name__)
# api = Api(app) # Api() replaced by ./routes/__init__.py
api.init_app(app)

if __name__ == '__main__':
  app.run(debug=True)