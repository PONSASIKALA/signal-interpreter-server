""" XML parser """

# pylint: disable=missing-function-docstring

import xml
import xml.etree.ElementTree as ET
import logging
import xmltodict

from signal_interpreter_server.exceptions import XmlParserError

logger = logging.getLogger(__name__)

class XmlParser:
    """ XML parser class """

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """ Load file """
		try:
        	tree = ET.parse(file_path)
			data = tree.getroot()
			xml_string = ET.tostring(data, encoding="utf-8", method="xml")
			data = dict(xmltodict.parse(xml_string))
        except FileNotFoundError as err:
            logger.exception('Could not find "%s"', file_path)
            raise XmlParserError from err

    def get_signal_title(self, identifier):
        """ Get signal title """
        for service in self.data["services"]:
            if service["id"] == identifier:
                return service["title"]
        raise XmlParserError(f'Identifier "{identifier}" is not available in the signal database.')
