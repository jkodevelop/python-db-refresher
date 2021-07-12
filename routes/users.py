from flask_restx import Namespace, Resource, fields
from flask import Flask, request
from neo4j import GraphDatabase

from util.config import config
from util.helpers import get_uid
from util.cypher.users import latest, getById

# driver = GraphDatabase.driver('neo4j://localhost:7687', auth=('neo4j', 'password'), encrypted=True, trust=False)
# session.write_transaction(add_friend, "Arthur", "Merlin")

def serialize_user(u):
  return {
    'first_name': u['firstname'],
    'last_name': u['lastname'],
  }

api = Namespace('users', description='Users management')

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class HelloWorld(Resource):
  def get(self):
    driver = GraphDatabase.driver(config['neo4j']['DB_CONN_STR'], auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.read_transaction(latest)
    driver.close()
    # print(records)
    return [serialize_user(record['u']) for record in records]

@api.route('/get/<id>',doc={ 
  'description': 'get user by ID'
})
@api.doc(params={'id': 'An ID'})
class ParamExample(Resource):
  def get(self, id):
    driver = GraphDatabase.driver('neo4j://localhost:7687', auth=(config['neo4j']['DB_USER'], config['neo4j']['DB_PASS']), encrypted=False)
    with driver.session(database=config['neo4j']['DB_DBNAME']) as session:
      records = session.read_transaction(getById,id)
    driver.close()
    # print(records)
    return [serialize_user(record['u']) for record in records]
