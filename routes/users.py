import json
from flask_restx import Namespace, Resource, fields
from flask import Flask, request, current_app
from pymongo import MongoClient, DESCENDING
from bson import json_util
from bson.objectid import ObjectId
import datetime

def parse_json(data):
    return json.loads(json_util.dumps(data))

api = Namespace('users', description='Users management')

user_obj =  api.model('user_obj', {
  'email': fields.String(default='example@example.com',description='email'),
  'firstname': fields.String(default='first name',description='first name'),
  'lastname': fields.String(default='last name',description='last name'),
})

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class Latest(Resource):
  def get(self):
    client = MongoClient(current_app.config.get('MONGO_URI'))
    mongo_dbname = current_app.config.get('MONGO_DBNAME')
    mongodb = client[mongo_dbname]
    user_collection = mongodb['user'] 
    res = []
    for row in user_collection.find().sort([('_id',DESCENDING)]).limit(1):
      res.append(parse_json(row))
    return res

@api.route('/get/<id>',doc={ 
  'description': 'get user by ID'
})
@api.doc(params={'id': 'An ID'})
class GetById(Resource):
  def get(self, id):
    client = MongoClient(current_app.config.get('MONGO_URI'))
    mongo_dbname = current_app.config.get('MONGO_DBNAME')
    mongodb = client[mongo_dbname]
    user_collection = mongodb['user'] 
    
    if not ObjectId.is_valid(id):
      return {'error':'invalid ObjectId'}

    res = []  
    for row in user_collection.find({'_id': ObjectId(id)}):
      res.append(parse_json(row))
    return res

@api.route('/create', doc={ 
  'description': 'insert example'
})
class CreateUser(Resource):
  @api.expect(user_obj, validate=True)
  def post(self):
    post_param = request.get_json()
    client = MongoClient(current_app.config.get('MONGO_URI'))
    mongo_dbname = current_app.config.get('MONGO_DBNAME')
    mongodb = client[mongo_dbname]
    user_collection = mongodb['user'] 
    
    user = {
      'email': post_param['email'],
      'firstname': post_param['firstname'],
      'lastname': post_param['lastname'],
      'created': datetime.datetime.utcnow()
    }
    user_id = user_collection.insert_one(user).inserted_id
    return {
      'status': 'success',
      'res': str(user_id)
    }
    api.abort(404, 'invalid: could not complete api call')

@api.route('/delete/<string:id>', doc={ 
  'description': 'delete example'
})
class DeleteUser(Resource):
  def delete(self, id):
    client = MongoClient(current_app.config.get('MONGO_URI'))
    mongo_dbname = current_app.config.get('MONGO_DBNAME')
    mongodb = client[mongo_dbname]
    user_collection = mongodb['user'] 
    result = user_collection.delete_one({'_id': ObjectId(id)})
    return {
      'status': 'success',
      'res': result.deleted_count
    }
    api.abort(404, 'invalid: could not complete api call')

@api.route('/update/<string:id>', doc={ 
  'description': 'update example'
})
class UpdateUser(Resource):
  @api.expect(user_obj, validate=True)
  def put(self, id):
    post_param = request.get_json()
    client = MongoClient(current_app.config.get('MONGO_URI'))
    mongo_dbname = current_app.config.get('MONGO_DBNAME')
    mongodb = client[mongo_dbname]
    user_collection = mongodb['user'] 
    
    user = {
      'email': post_param['email'],
      'firstname': post_param['firstname'],
      'lastname': post_param['lastname']
    }

    find_query = {'_id': ObjectId(id)}
    new_vals = { '$set': user }
    result = user_collection.update_one(find_query,new_vals)

    return {
      'status': 'success',
      'res': { 'matched': result.matched_count, 'modified': result.modified_count }
    }
    api.abort(404, 'invalid: could not complete api call')