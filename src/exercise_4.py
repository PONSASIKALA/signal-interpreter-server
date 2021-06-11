# routes.py
from flask import Flask, request

my_app = Flask(__name__)


@my_app.route("/", methods=["GET"])
def hello():
    return "Hello Hello hello World world!"


@my_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    return data


my_app.run()
