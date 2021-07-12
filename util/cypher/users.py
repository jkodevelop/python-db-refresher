from util.helpers import get_uid

def latest(tx):
  records = list()
  cypher = 'MATCH (u:User) RETURN u ORDER BY id(u) DESC LIMIT 1'
  for record in tx.run(cypher):
    records.append(record)
    print(record)
    print(record['u'])
  return records

def get_by_uid(tx,uid):
  cypher = 'MATCH (u:User{uid:toInteger($uid)}) RETURN u'
  return list(tx.run(cypher, uid=uid))

def create(tx,user):
  cypher = 'CREATE (u:User {uid:toInteger($uid),email:$email,firstname:$firstname,lastname:$lastname,active:$active}) RETURN u'
  return list(tx.run(cypher, 
    uid=get_uid(), email=user['email'],firstname=user['firstname'],lastname=user['lastname'],active=user['active']))
  # return record.single()[0]

def delete_by_uid(tx,uid):
  cypher = 'MATCH (u:User{uid:toInteger($uid)}) DELETE u'
  return tx.run(cypher, uid=uid)

def update_by_uid(tx,uid,user):
  cypher = 'MATCH (u:User{uid:toInteger($uid)}) SET u.email=$email,u.firstname=$firstname,u.lastname=$lastname,u.active=$active RETURN u'
  return list(tx.run(cypher, 
    uid=uid, email=user['email'],firstname=user['firstname'],lastname=user['lastname'],active=user['active']))