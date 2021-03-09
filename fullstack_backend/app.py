from flask import Flask

from fullstack_backend.extensions import db, migrate, jwt


def create_app(config_obj="fullstack_backend.config") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    configure_extensions(app)
    register_blueprints(app)
    configure_shell_context(app)
    configure_logger(app)
    register_commands(app)


def configure_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    return None


def register_blueprints(app: Flask):
    return None


def configure_shell_context(app: Flask):
    return None


def configure_logger(app: Flask):
    return None


def register_commands(app: Flask):
    return None
