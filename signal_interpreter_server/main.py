"""Main module"""
from argparse import ArgumentParser
from signal_interpreter_server.routes import signal_interpreter_app, json_parser


def parse_arguments():
    """ Parse arguments """
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()


def main():
    """ Main """
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    signal_interpreter_app.run()

def init():
    """ Init """
    if __name__ == "__main__":
        main()
		
init()
