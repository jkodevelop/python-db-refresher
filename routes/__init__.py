from flask_restx import Api

from .auth import api as auth_api
from .users import api as users_api

api = Api(
    title='Sample Flask RESTX starter',
    version='1.0',
    description='a simple start for Flask RESTX development'
)

api.add_namespace(auth_api, path='/api/auth')
api.add_namespace(users_api, path='/api/users')