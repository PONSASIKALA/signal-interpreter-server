""" JSON parser """
import json
import logging

from signal_interpreter_server.exceptions import JsonParserError

logger = logging.getLogger(__name__)


class JsonParser:
    """ JSON parser class """

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """ Load file """
        try:
            with open(file_path, "r") as json_file:
                self.data = json.load(json_file)
            logger.info("Loaded %s", file_path)
        except FileNotFoundError as err:
            logger.exception('Could not find "%s"', file_path)
            raise JsonParserError from err

    def get_signal_title(self, identifier):
        """ Get signal title """
        for service in self.data["services"]:
            if service["id"] == identifier:
                return service["title"]
        raise JsonParserError(f'Identifier "{identifier}" is not available in the signal database.')
