import pytest


from tests.unit import code_coverage
# from my-python-project.venv.src.signal-interpreter-server import code_coverage


@pytest.mark.parametrize("item, expected_result", [
    ("123", True),
    ("DEADBEEF", True),
    ("78AA", True),
    ("DUMMY", False),
    ("no hex", False),
])
def test_code_coverage(item, expected_result):
    assert code_coverage(item) == expected_result
