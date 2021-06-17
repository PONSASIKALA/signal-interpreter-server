""" Routes """
from flask import Flask, request, jsonify

from signal_interpreter_server.json_parser import JsonParser

signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """ Interpret signal """
    data = request.get_json()
    signal_title = json_parser.get_signal_title(data["signal"])
    return jsonify(signal_title)
