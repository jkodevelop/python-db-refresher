from flask_restx import Namespace, Resource, fields
from flask import Flask, request
import mysql.connector

from util.config import config

api = Namespace('db', description='Check db status')

@api.route('/status', doc={ 
  'description': 'get latest user'
})
class Status(Resource):
  def get(self):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor(dictionary=True)
    sql = 'SELECT VERSION()'
    cursor.execute(sql)
    data = cursor.fetchone()
    print ('Database version : %s ' % data)
    db.close()
    return {'database_version':data}
