""" Init """
# pylint: disable=missing-function-docstring

import logging.config
import os

import yaml

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
CFG_DIR = os.path.join(CURR_DIR, '..', 'cfg')
LOG_CONFIG_PATH = os.path.join(CFG_DIR, 'log_config.yaml')


with open(LOG_CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
