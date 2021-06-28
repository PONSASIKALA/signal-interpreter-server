from pytest import fixture


@fixture
def test_list():
    return ["one", "two", "three"]
