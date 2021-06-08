import sys
from functools import wraps
from flask import request

from flask_jwt_extended import (
    verify_jwt_in_request, get_jwt_identity
)

def token_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):

    if 'Authorization' in request.headers:
      check_truth = verify_jwt_in_request()
      print(f'--------\n{check_truth}\n--------', file=sys.stderr)

      jwt_id = get_jwt_identity()
      print(f'--------\n{jwt_id}\n--------', file=sys.stderr)

      if jwt_id == None:
        return {
          "status":"err",
          "msg":"not authorized"
        }, 403
      return fn(*args, **kwargs)
      
    else:
      return {
        "status":"err",
        "msg":"not authorized"
      }, 403
      
  return wrapper