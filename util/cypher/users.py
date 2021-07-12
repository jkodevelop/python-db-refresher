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