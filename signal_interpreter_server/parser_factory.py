# pylint: disable=missing-function-docstring
import logging
logger = logging.getLogger(__name__)


class ParserFactory:
    """ Parser Factor Class """
	
   def __init__(self):
        self._parsers = {}
        self._signal_database_format = None

    def set_signal_database_format(self, signal_database_format):
        self._signal_database_format = signal_database_format
        logger.debug("Signal database format is set to: %s", self._signal_database_format)

    def register_format(self, signal_database_format, parser):
        self._parsers[signal_database_format] = parser()
        logger.debug("Successfully registered a %s parser", signal_database_format)

    def get_parser(self):
        parser = self._parsers.get(self._signal_database_format)
        if not parser:
            logger.error("No valid parser could be found")
            raise ValueError(self._signal_database_format)
        return parser
