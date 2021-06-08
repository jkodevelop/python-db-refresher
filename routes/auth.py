import sys
from flask_restx import Namespace, Resource, fields
from flask import Flask, request, jsonify
from flask_jwt_extended import ( create_access_token )

from decorators.token_checker import token_required
from util.auth_options import api_key

api = Namespace('authentication', 
  description='example of authentication and protecting paths', 
  authorizations=api_key)

user = api.model('user', {
  'email': fields.String(required=True, default='email@email.com', description='login email'),
  'password': fields.String(required=True, default='****', description='login password')
})
  
@api.route('/login')
class Login(Resource):
  @api.expect(user, validate=True)
  def post(self):
    if not request.is_json:
      resp = jsonify({'err_msg': 'Missing JSON in request'})
      resp.status_code = 400
      return resp

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email or not password:
      resp = jsonify({"msg": "Bad email or password"})
      resp.status_code = 401
      return resp

    # "identity" can be any data that is json serializable
    access_token = create_access_token(identity=email)
    resp = jsonify(
      auth_token=access_token,
      msg='remember to use the word "Bearer" infront of the token' )
    resp.status_code = 200
    return resp    
    api.abort(404, 'invalid: could not complete api call')

@api.route('/protected', doc={ 
  'description': 'example of protected route, this requires authorization headers. Use the swagger Authorize options and put in the jwt auth_token from /api/auth/login'
})
class protected(Resource):
  @api.doc(security='apikey')
  @token_required
  def get(self):
    return { 'status': 'success' }