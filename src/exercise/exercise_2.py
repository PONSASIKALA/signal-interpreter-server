# routes.py
# pylint: disable=missing-function-docstring

from flask import Flask

my_app = Flask(__name__)


@my_app.route("/", methods=["GET"])
def hello():
    return "Hello Twi!"


my_app.run()
