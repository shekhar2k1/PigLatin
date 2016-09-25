#! ../env/bin/python

from flask import Flask

from views.main import main


def create_app(object_name):
    """
    A flask application factory
    """
    app = Flask(__name__)
    app.config.from_object(object_name)

    app.register_blueprint(main)

    return app

