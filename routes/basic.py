from flask_restx import Namespace, Resource, fields
from flask import Flask, request

api = Namespace('basic', description='basic examples')

basic_post =  api.model('basic_post', {
  'id': fields.String(required=True,description='id'),
  'active': fields.Boolean(required=True,default=True,description='active: true or false'),
  'text': fields.String(default='some text',description='text')
})

@api.route('/example')
class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

  @api.expect(basic_post, validate=True)
  def post(self):
    post_param = request.get_json()
    return {
      'status': 'success',
      'res': post_param
    }
    api.abort(404, 'invalid: could not complete api call')
