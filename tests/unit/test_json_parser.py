""" Unit tests for json_parser.py """
# pylint: disable=missing-function-docstring

from unittest.mock import patch, mock_open

import pytest

from signal_interpreter_server.exceptions import JsonParserError
from signal_interpreter_server.json_parser import JsonParser

VALID_JSON_DATA = '{ "json" : "This is a JSON" }'
PARSED_JSON_DATA = {"json": "This is a JSON"}


def test_load_file_with_valid_file(json_parser_instance):
    with patch("builtins.open", mock_open(read_data=VALID_JSON_DATA)):
        json_parser_instance.load_file("path/to/json/file")
        assert json_parser_instance.data == PARSED_JSON_DATA


def test_load_file_with_invalid_file(json_parser_instance):
    with pytest.raises(JsonParserError):
        json_parser_instance.load_file("invalid/file/path")


def test_get_signal_title_with_valid_identifier(json_parser_instance):
    assert json_parser_instance.get_signal_title("11") == "ECU Reset"


def test_get_signal_title_with_invalid_identifier(json_parser_instance):
    with pytest.raises(JsonParserError):
        json_parser_instance.get_signal_title("99")
