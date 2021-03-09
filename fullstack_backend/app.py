import logging
import os
import pprint
from logging.handlers import RotatingFileHandler

from flask import Flask

from fullstack_backend.api.v1 import api_v1
from fullstack_backend.database.models import Category, Post, PostCategory
from fullstack_backend.extensions import db, jwt, migrate


def create_app(config_obj="fullstack_backend.config") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    configure_extensions(app)
    register_blueprints(app)
    configure_logger(app)

    if app.config["TESTING"] is False:
        register_commands(app)
        configure_shell_context(app)

    return app


def configure_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(api_v1)


def configure_shell_context(app: Flask):
    def shell_context():
        """Shell context objects."""

        return {
            "db": db,
            "Post": Post,
            "Category": Category,
            "PostCategory": PostCategory,
        }

    app.shell_context_processor(shell_context)


def configure_logger(app: Flask):
    if app.config["ENV"] in ["development", "production"]:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/fullstack-backend.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(
            logging.DEBUG if app.config.get("ENV") == "development" else logging.INFO
        )
        app.logger.addHandler(file_handler)

    if app.config["ENV"] == "development" and app.config["LOG_TO_STDOUT"]:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG if app.config["DEBUG"] else logging.INFO)
        app.logger.addHandler(stream_handler)

    app.logger.info("DailyMenu API Initialized")
    app.logger.setLevel(logging.DEBUG if app.config["DEBUG"] else logging.INFO)
    app.logger.debug(f":: App Config ::\n{pprint.pformat(app.config)}")


def register_commands(app: Flask):
    pass
