from flask_restx import Namespace, Resource, fields
from flask import Flask, request

api = Namespace('basic', description='basic examples')

basic_post =  api.model('basic_post', {
  'id': fields.String(required=True,description='id'),
  'active': fields.Boolean(required=True,default=True,description='active: true or false'),
  'text': fields.String(default='some text',description='text')
})

@api.route('/example', doc={ 
  'description': 'example APIs of GET and POST'
})
class HelloWorld(Resource):
  def get(self):
    return {'hello':'world'}

  @api.expect(basic_post, validate=True)
  def post(self):
    post_param = request.get_json()
    return {
      'status': 'success',
      'res': post_param
    }
    api.abort(404, 'invalid: could not complete api call')

parent = api.model('parent', {
    'name': fields.String,
    'class': fields.String(discriminator=True)
})
child = api.inherit('child', parent, {
    'child_extra': fields.String
})

@api.route('/post/complexmodel', doc={ 
  'description': 'example of POST using a complex model Child inherit(Parent) restx-documentations'
})
class MorePostExample(Resource):
  @api.expect(child, validate=True)
  def post(self):
    post_param = request.get_json()
    return {
      'status': 'success',
      'res': post_param
    }
    api.abort(404, 'invalid: could not complete api call')

@api.route('/query',doc={ 
  'description': 'example of using url query parameters'
})
@api.doc(params={
  'first_name': {'in': 'query', 'description': 'First name of user', 'default': 'John', 'required':True},
  'middle_name': {'in': 'query', 'description': 'Middle name of user', 'default': 'Mid'},
  'last_name': {'in': 'query', 'description': 'Last name of user', 'default': 'Doe', 'required':True}
})
class QueryExample(Resource):
  def get(self):
    f_name = request.args.get('first_name')
    l_name = request.args.get('last_name')
    m_name = request.args.get('middle_name')
    if m_name is None:
      m_name = ' '
    else:
      m_name = f' {m_name} '

    return {
      'status': 'success',
      'full_name': f'{f_name}{m_name}{l_name}'
    }

@api.route('/urlparam/<id>',doc={ 
  'description': 'example of url with path parameter'
})
@api.doc(params={'id': 'An ID'})
class ParamExample(Resource):
  def get(self, id):
    return {'id':id}

@api.route('/urlparams/<id>/filter/<value>',doc={ 
  'description': 'example of url with multiple path parameter (order matters)'
})
@api.doc(params={
  'id': 'An ID',
  'value': 'A String Value'
})
class ParamsExample(Resource):
  def get(self, id, value):
    return {
      'id':id,
      'value': value
    }

@api.route('/combined/<id>/params',doc={ 
  'description': 'example of using all parameters, path/query/post body + documentation'
})
@api.doc(params={
  'id': 'An ID',
  'query_param': {'in': 'query', 'description': 'query parameter in url', 'default': 'Testing', 'required':True}
})
class ParamExample(Resource):
  @api.expect(basic_post, validate=True)
  def post(self, id):
    q_val = request.args.get('query_param')
    post_param = request.get_json()
    return {
      'id':id,
      'query': q_val,
      'post_param': post_param
    }