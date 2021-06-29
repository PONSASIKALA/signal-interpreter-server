""" Unit tests for main.py """
from unittest.mock import patch

from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.main import main, ArgumentParser, parse_arguments, init
from signal_interpreter_server.routes import signal_interpreter_app


class MockArguments:
    file_path = "path/to/file"


@patch.object(ArgumentParser, "parse_args", return_value=MockArguments)
@patch.object(ArgumentParser, "add_argument")
def test_parse_arguments(mock_add_argument, mock_parse_args):
    assert parse_arguments() == MockArguments
    mock_add_argument.assert_called_with("--file_path")
    mock_parse_args.assert_called_once()


@patch.object(signal_interpreter_app, "run")
@patch.object(JsonParser, "load_file")
@patch("signal_interpreter_server.main.parse_arguments", return_value=MockArguments)
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    main()
    mock_parse_arguments.assert_called_once()
    mock_load_file.assert_called_with(MockArguments.file_path)
    mock_run.assert_called_once()


def test_init():
    with patch("signal_interpreter_server.main.main") as mock_main:
        with patch("signal_interpreter_server.main.__name__", "__main__"):
            init()
            mock_main.assert_called_once()
