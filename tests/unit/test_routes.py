""" Unit tests for routes.py """
# pylint: disable=missing-function-docstring, missing-class-docstring
from unittest.mock import patch

import pytest

from signal_interpreter_server.routes import parser_factory, SignalInterpreterServerException
from signal_interpreter_server.parser_factory import ParserFactory
from signal_interpreter_server.json_parser import JsonParser


@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
                        ({"signal": "11"}, 200, "ECU Reset"),
                        ({"dummy": "27"}, 400, None)
])
def test_interpret_signal(payload, expected_status_code, expected_response, signal_interpreter_app_instance):
    with signal_interpreter_app_instance as client:
        with patch.object(JsonParser, "get_signal_title", return_value=expected_response):
            with patch.object(parser_factory, "get_parser", return_value=JsonParser):
                response = client.post("/", json=payload)
                assert response.get_json() == expected_response
                assert response.status_code == expected_status_code


def test_interpret_signal_with_signal_not_found(signal_interpreter_app_instance):
    with signal_interpreter_app_instance as client:
        with patch.object(JsonParser, "get_signal_title", side_effect=JsonParserError):
            with patch.object(parser_factory, "get_parser", return_value=JsonParser):
                response = client.post("/", json={"signal": "99"})
                assert response.get_json() is None
                assert response.status_code == 404


def test_interpret_signal_with_invalid_parser(signal_interpreter_app_instance):
    with patch.object(ParserFactory, "get_parser", side_effect=JsonParserError):
        with signal_interpreter_app_instance as client:
            response = client.post("/", json={"signal": "11"})
            assert response.get_json() is None
            assert response.status_code == 500
