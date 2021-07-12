from flask_restx import Namespace, Resource, fields
from flask import Flask, request
from neo4j import GraphDatabase

from util.config import config
from util.cypher.users import latest, get_by_uid, create, delete_by_uid, update_by_uid

# driver = GraphDatabase.driver('neo4j://localhost:7687', auth=('neo4j', 'password'), encrypted=True, trust=False)
# session.write_transaction(add_friend, "Arthur", "Merlin")

def serialize_user(u):
  return {
    'uid': u['uid'],
    'first_name': u['firstname'],
    'last_name': u['lastname'],
    'email': u['email'],
    'active': u['active']
  }

api = Namespace('users', description='Users management')

user_node =  api.model('basic_post', {
  'email': fields.String(required=True, description='email of user'),
  'firstname': fields.String(required=True, default='',description='first name'),
  'lastname': fields.String(required=True, default='',description='last name'),
  'active': fields.Boolean(default=False,description='active: true or false')
})

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class Latest(Resource):
  def get(self):
    driver = GraphDatabase.driver(config['neo4j']['DB_CONN_STR'], auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.read_transaction(latest)
    driver.close()
    # print(records)
    return [serialize_user(record['u']) for record in records]

@api.route('/get/<int:uid>',doc={ 
  'description': 'get user by UID'
})
@api.doc(params={'uid': 'An ID'})
class GetUID(Resource):
  def get(self, uid):
    driver = GraphDatabase.driver(config['neo4j']['DB_CONN_STR'], auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.read_transaction(get_by_uid,uid)
    driver.close()
    print(records)
    return [serialize_user(record['u']) for record in records]

@api.route('/create', doc={ 
  'description': 'create a User node'
})
class CreateUser(Resource):
  @api.expect(user_node, validate=True)
  def post(self):
    post_param = request.get_json()
    driver = GraphDatabase.driver(config['neo4j']['DB_CONN_STR'], auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.write_transaction(create,post_param)
    driver.close()
    print(records)
    return serialize_user(records[0]['u'])
    api.abort(404, 'invalid: could not complete api call')

@api.route('/delete/<int:uid>', doc={ 
  'description': 'delete a User node by uid'
})
@api.doc(params={'uid': 'An ID'})
class DeleteUser(Resource):
  def delete(self, uid):
    driver = GraphDatabase.driver(config['neo4j']['DB_CONN_STR'], auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.write_transaction(delete_by_uid,uid)
    driver.close()
    # print(records)
    # print(records.single())
    return { 'status':'success' }
    api.abort(404, 'invalid: could not complete api call')

@api.route('/update/<int:uid>', doc={ 
  'description': 'update a user node attributes'
})
@api.doc(params={'uid': 'An ID'})
class UpdateUser(Resource):
  @api.expect(user_node, validate=True)
  def put(self, uid):
    post_param = request.get_json()
    driver = GraphDatabase.driver(config['neo4j']['DB_CONN_STR'], auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.write_transaction(update_by_uid,uid,post_param)
    driver.close()
    print(records)
    if len(records) == 0:
      return { 'status':'no records updated' }
    else:
      return serialize_user(records[0]['u'])
    api.abort(404, 'invalid: could not complete api call')