""" Shared fixtures """
# pylint: disable=missing-function-docstring

import pytest

from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import ParserFactory
from signal_interpreter_server.routes import signal_interpreter_app


@pytest.fixture
def signal_interpreter_app_instance():
    signal_interpreter_app.testing = True
    return signal_interpreter_app.test_client()

@pytest.fixture
def json_parser_instance():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "Security Access", "id": "27"}]}
    return json_parser

@pytest.fixture
def xml_parser_instance():
    xml_parser = ParserFactory()
    xml_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "Security Access", "id": "27"}]}
    return xml_parser
