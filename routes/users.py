import json
from flask_restx import Namespace, Resource, fields
from flask import Flask, request, current_app
from pymongo import MongoClient, DESCENDING
from bson import json_util
from bson.objectid import ObjectId

def parse_json(data):
    return json.loads(json_util.dumps(data))

api = Namespace('users', description='Users management')

# client = MongoClient('mongodb://localhost:27017/')

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class HelloWorld(Resource):
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
class ParamExample(Resource):
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
