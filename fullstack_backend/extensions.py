from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from passlib.context import CryptContext

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
