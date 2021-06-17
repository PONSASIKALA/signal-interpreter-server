import os
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
""" run on tests folder in local PC"""
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")


@task
def style(c):
    c.run(f"pycodestyle {SRC_DIR} --ignore=E501")


@task
def lint(c):
    c.run(f"pylint {SRC_DIR}")


@task
def unit_test(c):
    ignore_ex = "--ignore exercise_1 --ignore exercise_2 --ignore exercise_3 --ignore exercise_4 --ignore exercise_5"
    return_value = c.run(f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH} --verbose {ignore_ex}")
    
    if return_value == 0:
        print("Success!")
    else:
        print(f'Failed to run:\n"{cmd}"\nwith exit code: {return_value}')
