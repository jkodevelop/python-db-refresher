from flask_restx import Api

from .basic import api as basic_api
from .fileio import api as fileio_api
from .auth import api as auth_api

api = Api(
    title='Sample Flask RESTX starter',
    version='1.0',
    description='a simple start for Flask RESTX development'
)

api.add_namespace(basic_api, path='/api/basic')
api.add_namespace(fileio_api, path='/api/fileio')
api.add_namespace(auth_api, path='/api/auth')