from flask_restx import Namespace, Resource, fields
from flask import Flask, request
import pymysql

from util.config import config

api = Namespace('users', description='Users management')

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class Latest(Resource):
  def get(self):
    db = pymysql.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'],
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT `id`,`email`,`firstname`,`lastname` FROM `users` ORDER BY `id` DESC'
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
    db = pymysql.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'],
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT `id`,`email`,`firstname`,`lastname` FROM `users` WHERE `id`=%s'
    cursor.execute(sql,(id,))
    data = cursor.fetchone()
    print ('db result: %s ' % data)
    db.close()
    return data