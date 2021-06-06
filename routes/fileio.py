import sys,os
from flask_restx import Namespace, Resource, fields, reqparse
from flask import Flask, request
from werkzeug.datastructures import FileStorage

api = Namespace('fileupload', description='file handling examples')

file_upload = reqparse.RequestParser()
file_upload.add_argument('file_obj',  
                         type=FileStorage, 
                         location='files', 
                         required=True, 
                         help='file')

def process_file(file_object):
  print(file_object.mimetype, file=sys.stderr)
  # print(file_object.name, file=sys.stderr) # useless, name is just name
  print(file_object.filename, file=sys.stderr)

  destination = os.path.join(os.getcwd(), 'uploads',file_object.filename)
  print(destination)

  save_result = file_object.save(destination)
  print(save_result)
  return destination
  
@api.route('/upload')
class UploadExample(Resource):
  @api.expect(file_upload)
  def post(self):
    args = file_upload.parse_args()
    print('----------------', file=sys.stderr)
    print(args, file=sys.stderr)
    saved_path = process_file(args['file_obj'])
    print('----------------', file=sys.stderr)
    return {
      'status': 'success',
      'path': saved_path
    }
    api.abort(404, 'invalid: could not complete api call')
