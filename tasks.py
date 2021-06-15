import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
""" run on tests folder in local PC"""
SRC_DIR = os.path.join(CURR_DIR, "signal-interpreter-server-main")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")

@task
def style(_):
    call(f"pycodestyle {SRC_DIR} --ignore=E501", shell=True)

@task
def lint(_):
    call(f"pylint {SRC_DIR}", shell=True)

@task
def unit_test(_):
    call(f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH} --verbose")
    return_value = call(cmd, shell=True)
    if return_value == 0:
        print("Success!")
    else:
        print(f'Failed to run:\n"{cmd}"\nwith exit code: {return_value}')
