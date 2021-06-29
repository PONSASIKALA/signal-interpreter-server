""" Main """
# pylint: disable=missing-function-docstring

import logging
from argparse import ArgumentParser

from signal_interpreter_server.routes import json_parser, signal_interpreter_app

logger = logging.getLogger(__name__)


def parse_arguments():
    """ Parse arguments """
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    args = parser.parse_args()
    logger.debug("Got arguments %s", args)
    return args


def main():
    """ Main """
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    logger.debug("Starting signal interpreter server")
    signal_interpreter_app.run()


def init():
    """ Init """
    if __name__ == "__main__":
        main()


init()
