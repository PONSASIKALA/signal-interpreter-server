""" Routes """
# pylint: disable=missing-function-docstring

import logging

from flask import Flask, request, jsonify, abort

from signal_interpreter_server.exceptions import JsonParserError
from signal_interpreter_server.exceptions import XmlParserError
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import ParserFactory

signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()
xml_parser = ParserFactory()

logger = logging.getLogger(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """ Interpret signal """
    data = request.get_json()
    logger.info("Received data: %s", data)
    try:
        signal_title = json_parser.get_signal_title(data["signal"])
        signal_title = ParserFactory.get_signal_title(data["signal"])
        logger.info("Signal title: %s", signal_title)
        return jsonify(signal_title)
    except KeyError as err:
        logger.exception("Received error %s", err)
        abort(400, description=f"Payload {data} is not correct, expects the key to be 'signal'.")
    except JsonParserError as err:
        logger.exception("Received error %s", err)
        abort(404, description=f"Interpretation for {data['signal']} not available.")
    except XmlParserError as err:
        logger.exception("Received error %s", err)
        abort(404, description=f"Interpretation for {data['signal']} not available.")
