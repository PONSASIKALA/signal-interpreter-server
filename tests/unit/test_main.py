""" Unit tests for main.py """
# pylint: disable=missing-function-docstring

from unittest.mock import patch

from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.main import parse_arguments, ArgumentParser, parser_factory, register_parsers
from signal_interpreter_server.main import load_database, main, init
from signal_interpreter_server.routes import signal_interpreter_app


class MockArguments:  # pylint: disable=too-few-public-methods
    file_path = "file_path.json"


@patch.object(ArgumentParser, "parse_args", return_value=MockArguments)
@patch.object(ArgumentParser, "add_argument")
def test_parse_arguments(mock_add_argument, mock_parse_args):
    assert parse_arguments() == MockArguments
    mock_add_argument.assert_called_with("--file_path")
    mock_parse_args.assert_called_once()


def test_register_parsers():
    with patch.object(parser_factory, "register_format") as mock_register_parser:
        register_parsers()
        mock_register_parser.assert_called()


def test_load_file():
    with patch.object(parser_factory, "set_signal_database_format") as mock_set_signal_database_format:
        with patch.object(JsonParser, "load_file") as mock_load_file:
            with patch.object(parser_factory, "get_parser", return_value=JsonParser) as mock_get_parser:
                load_database("file_path.json")
                mock_set_signal_database_format.assert_called_once()
                mock_get_parser.assert_called_once()
                mock_load_file.assert_called_with("file_path.json")


@patch.object(signal_interpreter_app, "run")
def test_main(mock_run):
    with patch("signal_interpreter_server.main.parse_arguments", return_value=MockArguments) as mock_parse_arguments:
        with patch("signal_interpreter_server.main.register_parsers") as mock_register_parsers:
            with patch("signal_interpreter_server.main.load_database") as mock_load_database:
                main()
                mock_parse_arguments.assert_called_once()
                mock_register_parsers.assert_called_once()
                mock_load_database.assert_called_with("file_path.json")
                mock_run.assert_called_once()


def test_init():
    with patch("signal_interpreter_server.main.main") as mock_main:
        with patch("signal_interpreter_server.main.__name__", "__main__"):
            init()
            mock_main.assert_called_once()
