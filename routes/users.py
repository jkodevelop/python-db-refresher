from flask_restx import Namespace, Resource, fields
from flask import Flask, request
import mysql.connector

from util.config import config

api = Namespace('users', description='Users management')

@api.route('/latest', doc={ 
  'description': 'get latest user'
})
class Latest(Resource):
  def get(self):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor(dictionary=True)
    sql = 'SELECT `id`,`email`,`firstname`,`lastname` FROM `users` ORDER BY `id` DESC'
    cursor.execute(sql)
    data = cursor.fetchone()
    print ('db result: %s ' % data)
    db.close()
    return data

@api.route('/get/<int:id>',doc={ 
  'description': 'get user by ID'
})
@api.doc(params={'id': 'An ID'})
class GetById(Resource):
  def get(self, id):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor(dictionary=True)
    sql = 'SELECT `id`,`email`,`firstname`,`lastname` FROM `users` WHERE `id`=%s'
    cursor.execute(sql,(id,))
    data = cursor.fetchone()
    print ('db result: %s ' % data)
    db.close()
    return data

@api.route('/procedure/getusers',doc={ 
  'description': 'example of calling a stored procedure'
})
class StoreProcedureGetExample(Resource):
  def get(self):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor()
    args = cursor.callproc('get_users')
    print("Return value:", args)
    for result in cursor.stored_results():
      print ('stored_results: %s ' % result)
      data = result.fetchall()
      print ('results: %s ' % data)

    db.close()
    return data

@api.route('/procedure/inactivateall',doc={ 
  'description': 'example of calling a stored procedure'
})
class ProcedureInactive(Resource):
  def get(self):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor()
    args = cursor.callproc('set_all_inactive')

    print("Return value:", args)
    for result in cursor.stored_results():
      print ('stored_results: %s ' % result)

    db.commit() # this is required for all procedure that changes database values
    db.close()
    return { 'status':'success' }

@api.route('/procedure/activateall',doc={ 
  'description': 'example of calling a stored procedure'
})
class ProcedureActive(Resource):
  def get(self):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor()
    args = cursor.callproc('set_all_active')

    print("Return value:", args)
    for result in cursor.stored_results():
      print ('stored_results: %s ' % result)

    db.commit() # this is required for all procedure that changes database values
    db.close()
    return { 'status':'success' }

@api.route('/procedure/setactive/<string:active>/id/<int:id>',doc={ 
  'description': 'example of calling a stored procedure with input params'
})
@api.doc(params={
  'active': 'set to True or False',
  'id': 'An ID'
})
class ProcedureWithInput(Resource):
  def put(self, active, id):
    db = mysql.connector.connect(host=config['mysql']['DB_HOST'],
                        user=config['mysql']['DB_USER'],
                        password=config['mysql']['DB_PASS'],
                        database=config['mysql']['DB_DBNAME'])
    cursor = db.cursor()
    active_value = 0
    if active.lower() == 'true':
      active_value = 1
    args = cursor.callproc('set_active',(active_value, id))
    print("Return value:", args)
    for result in cursor.stored_results():
      print ('stored_results: %s ' % result)

    db.commit() # this is required for all procedure that changes database values
    db.close()
    return { 'status':'success' }