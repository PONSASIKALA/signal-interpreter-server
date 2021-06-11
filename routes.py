from flask import Flask, request

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def mirror_payload():
    data = request.get_json()
    return data
