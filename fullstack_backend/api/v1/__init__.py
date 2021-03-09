from flask import Blueprint
from flask_restx import Api

api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api = Api(api_v1, version="1.0", title="Full Stack Backend API")
