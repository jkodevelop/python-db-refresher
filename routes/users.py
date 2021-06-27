from flask_restx import Namespace, Resource, fields
from flask import Flask, request
import pymysql

api = Namespace('users', description='Users management')

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class Latest(Resource):
  def get(self):
    db = pymysql.connect(host='localhost',
                        user='zzz',
                        password='sapassword',
                        database='zzz',
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT `id`,`email`,`first_name`,`last_name` FROM `users` ORDER BY `id` DESC'
    cursor.execute(sql)
    data = cursor.fetchone()
    print ('db result: %s ' % data)
    db.close()
    return data

@api.route('/get/<id>',doc={ 
  'description': 'get user by ID'
})
@api.doc(params={'id': 'An ID'})
class GetById(Resource):
  def get(self, id):
    db = pymysql.connect(host='localhost',
                        user='zzz',
                        password='sapassword',
                        database='zzz',
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT `id`,`email`,`first_name`,`last_name` FROM `users` WHERE `id`=%s'
    cursor.execute(sql,(id,))
    data = cursor.fetchone()
    print ('db result: %s ' % data)
    db.close()
    return data