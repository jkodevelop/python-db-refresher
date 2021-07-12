from flask_restx import Namespace, Resource, fields
from flask import Flask, request
import pymysql

from util.config import config

api = Namespace('db', description='Check db status')

@api.route('/status', doc={ 
  'description': 'get latest user'
})
class Status(Resource):
  def get(self):
    db = pymysql.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'],
                        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT VERSION()'
    cursor.execute(sql)
    data = cursor.fetchone()
    print ('Database version : %s ' % data)
    db.close()
    return {'database_version':data}
