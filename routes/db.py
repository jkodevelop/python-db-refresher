from flask_restx import Namespace, Resource, fields
from flask import Flask, request
import pymysql

api = Namespace('db', description='Check db status')

@api.route('/status', doc={ 
  'description': 'get latest user'
})
class Status(Resource):
  def get(self):
    db = pymysql.connect(host='localhost',
                        user='zzz',
                        password='sapassword',
                        database='zzz',
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT VERSION()'
    cursor.execute(sql)
    data = cursor.fetchone()
    print ('Database version : %s ' % data)
    db.close()
    return {'database_version':data}
