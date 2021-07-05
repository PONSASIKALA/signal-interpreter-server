from unittest.mock import patch, mock_open

from signal_interpreter_server.xml_parser import ParserFactory


VALID_XML_DATA = '{ "xml" : "This is a XML" }'
PARSED_XML_DATA = {"xml": "This is a XML"}


def test_load_file():
    with patch("builtins.open", mock_open(read_data=VALID_XML_DATA)):
        xml_parser = ParserFactory()
        xml_parser.load_file("path/to/xml/file")
        assert xml_parser.data == PARSED_XML_DATA


def test_get_signal_title():
    xml_parser = ParserFactory()
    xml_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert xml_parser.get_signal_title("11") == "ECU Reset"
