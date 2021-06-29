""" Integration tests for interpreting a signal """
# pylint: disable=missing-function-docstring

import os
import sys
from unittest.mock import patch

import pytest

from signal_interpreter_server.main import main
from signal_interpreter_server.routes import signal_interpreter_app

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_BASIC_FIXTURE_PATH = os.path.join(CURR_DIR, "fixtures", "test_basic.json")


@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "99"}, 200, "ECU Reset"),
    ({"signal": "98"}, 404, None),
    ({"DUMMY": "27"}, 400, None)
])
@patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", TEST_BASIC_FIXTURE_PATH])
def test_interpret_signal(payload, expected_status_code, expected_response, signal_interpreter_app_instance):
    with patch.object(signal_interpreter_app, "run"):
        with signal_interpreter_app_instance as client:
            main()
            response = client.post("/", json=payload)
            assert response.get_json() == expected_response
            assert response.status_code == expected_status_code
