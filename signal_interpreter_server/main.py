""" Main """
# pylint: disable=missing-function-docstring

import logging
from argparse import ArgumentParser

from signal_interpreter_server.routes import json_parser, signal_interpreter_app, parser_factory
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import XmlParser

logger = logging.getLogger(__name__)


def parse_arguments():
    """ Parse arguments """
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    args = parser.parse_args()
    logger.debug("Got arguments %s", args)
    return args


def register_parsers():
    """ Register parsers """
    parser_factory.register_format("JSON", JsonParser)
    parser_factory.register_format("XML", XmlParser)


def load_database(file_path):
    """ Load database """
    signal_database_format = file_path.split(".")[-1].upper()
    parser_factory.set_signal_database_format(signal_database_format)
    parser = parser_factory.get_parser()
    parser.load_file(file_path)


def main():
    """ Main """
    args = parse_arguments()
    register_parsers()
    load_database(args.file_path)
    signal_interpreter_app.run()


def init():
    """ Init """
    if __name__ == "__main__":
        main()


init()
