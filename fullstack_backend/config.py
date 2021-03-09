import os
from dotenv import load_dotenv

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.pardir(HERE)

load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

FLASK_APP = os.environ.get('FLASK_APP')
FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
FLASK_ENV = os.environ.get("FLASK_ENV")
SECRET_KEY = os.environ.get("SECRET_KEY", 'something-something-darkside')
SERVER_NAME = os.getenv("SERVER_NAME", None)

ENV = FLASK_ENV
DEBUG = FLASK_ENV == "development"

# Logging options
LOG_LEVEL = os.environ.get("LOG_LEVEL", "info")
LOG_TO_STDOUT = os.getenv("LOG_TO_STDOUT", False)

# Database Config
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)

