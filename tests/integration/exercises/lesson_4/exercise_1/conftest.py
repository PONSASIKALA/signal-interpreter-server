# pylint: disable=missing-function-docstring

from pytest import fixture


@fixture
def test_list():
    return ["one", "two", "three"]
