from flask_restx import Namespace, Resource, fields
from flask import Flask, request
from neo4j import GraphDatabase

# driver = GraphDatabase.driver('neo4j://localhost:7687', auth=('neo4j', 'password'), encrypted=True, trust=False)
# session.write_transaction(add_friend, "Arthur", "Merlin")

def serialize_user(u):
  return {
    'first_name': u['firstname'],
    'last_name': u['lastname'],
  }

def latest(tx):
  records = list()
  cypher = 'MATCH (u:User) RETURN u ORDER BY id(u) DESC LIMIT 1'
  for record in tx.run(cypher):
    records.append(record)
    print(record)
    print(record['u'])
  return records

def getById(tx,id):
  cypher = 'MATCH (u) WHERE id(u)=toInteger($id) RETURN u'
  return list(tx.run(cypher, id=id))

api = Namespace('users', description='Users management')

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class HelloWorld(Resource):
  def get(self):
    driver = GraphDatabase.driver('neo4j://localhost:7687', auth=('zzz', 'npassword'), encrypted=False)
    with driver.session(database='zzz') as session:
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
    driver = GraphDatabase.driver('neo4j://localhost:7687', auth=('zzz', 'npassword'), encrypted=False)
    with driver.session(database='zzz') as session:
      records = session.read_transaction(getById,id)
    driver.close()
    # print(records)
    return [serialize_user(record['u']) for record in records]
