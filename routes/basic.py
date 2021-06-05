from flask_restx import Namespace, Resource

api = Namespace('basic', description='basic examples')

@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}