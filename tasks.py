""" Tasks to perform style, lint and test """
import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
""" run on tests folder in local PC"""
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")
EXER_DIR = os.path.join(UNIT_TEST_DIR, "exercises")
LOG_SETTINGS_PATH = os.path.join(CURR_DIR, "..", "cfg", "log_settings.yaml")
FIXTURE_PATH = os.path.join(CURR_DIR, "..", "fixture", "test_basic.json")
INTEGRATION_TEST_DIR = os.path.join(CURR_DIR, "tests", "integration")

@task
def style(_):
    """ Style check """
    call(f"pycodestyle {SRC_DIR} --ignore=E501", shell=True)

@task
def lint(_):
    """ Lint check """
    call(f"pylint {SRC_DIR}", shell=True)

@task
def unit_test(_):
    """ Run unit tests """
    call(f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH} --verbose")
	
	
@task
def integration_test(_):
    """ Run integration tests """
    call(f"pytest {INTEGRATION_TEST_DIR} --verbose")
