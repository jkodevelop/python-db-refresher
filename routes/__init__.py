from flask_restx import Api

from .basic import api as basic_api

api = Api(
    title='Sample Flask RESTX starter',
    version='1.0',
    description='a simple start for Flask RESTX development'
)

api.add_namespace(basic_api, path="/api/basic")