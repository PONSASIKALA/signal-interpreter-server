from unittest.mock import patch, mock_open

from collections import OrderedDict
import pytest

from signal_interpreter_server.xml_parser import XmlParserError


def test_load_file(xml_parser_instance):
    with patch('builtins.open', mock_open(read_data='<services><service id="11"><title>ECU Reset</title>'
                                                    '</service></services>')):
        xml_parser_instance.load_file('path/to/file')
        assert xml_parser_instance.data == {
            'services': OrderedDict([('service', OrderedDict([('@id', '11'), ('title', 'ECU Reset')]))])
        }


def test_load_file_2(xml_parser_instance):
    with patch("xml.etree.ElementTree.parse") as mock_parse:
        with patch("xml.etree.ElementTree.tostring") as mock_to_string:
            with patch("xmltodict.parse") as mock_xml_to_dict_parse:
                xml_parser_instance.load_file("path_to_file")
                mock_parse.assert_called_with("path_to_file")
                mock_to_string.assert_called_once()
                mock_xml_to_dict_parse.assert_called_once()


def test_load_file_with_invalid_file(xml_parser_instance):
    with pytest.raises(XmlParserError):
        xml_parser_instance.load_file("invalid/file/path")


def test_get_signal_title_with_valid_identifier(xml_parser_instance):
    assert xml_parser_instance.get_signal_title("11") == "ECU Reset"


def test_get_signal_title_with_invalid_identifier(xml_parser_instance):
    with pytest.raises(XmlParserError):
        xml_parser_instance.get_signal_title("99")
