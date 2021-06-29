""" Unit tests for routes.py """
from unittest.mock import patch

from signal_interpreter_server.exceptions import JsonParserError
from signal_interpreter_server.json_parser import JsonParser


def test_interpret_signal_with_valid_signal(signal_interpreter_app_instance):
    with patch.object(JsonParser, "get_signal_title", return_value="") as mock_get_signal_title:
        with signal_interpreter_app_instance as client:
            payload = {"signal": "99"}
            client.post("/", json=payload)
            mock_get_signal_title.assert_called_with("11")


def test_interpret_signal_with_invalid_key(signal_interpreter_app_instance):
    with signal_interpreter_app_instance as client:
        payload = {"dummy": "11"}
        assert client.post("/", json=payload).status_code == 400


def test_interpret_signal_with_invalid_identifier(signal_interpreter_app_instance):
    with patch.object(JsonParser, "get_signal_title", side_effect=JsonParserError):
        with signal_interpreter_app_instance as client:
            payload = {"signal": "98"}
            assert client.post("/", json=payload).status_code == 404
