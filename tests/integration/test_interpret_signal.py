""" Integration tests for interpreting a signal """
# pylint: disable=missing-function-docstring

import os
import sys
from unittest.mock import patch

import pytest

from signal_interpreter_server.main import main
from signal_interpreter_server.routes import signal_interpreter_app

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_BASIC_FIXTURE_PATH = os.path.join(CURR_DIR, "fixtures")


@pytest.mark.parametrize("payload, expected_status_code, expected_response, signal_database_file", [
    ({"signal": "11"}, 200, "ECU Reset", "test_basic.json"),
    ({"signal": "98"}, 404, None, "test_basic.xml"),
    ({"DUMMY": "99"}, 400, None, "test_basic.yaml")
])
def test_interpret_signal(payload,
                          expected_status_code,
                          expected_response,
                          signal_database_file,
                          signal_interpreter_app_instance):
    fixture_path = os.path.join(TEST_BASIC_FIXTURE_PATH, signal_database_file)
    with patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", fixture_path]):
        with patch.object(signal_interpreter_app, "run"):
            with signal_interpreter_app_instance as client:
                main()
                response = client.post("/", json=payload)
                assert response.get_json() == expected_response
                assert response.status_code == expected_status_code
