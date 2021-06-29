# pylint: disable=missing-function-docstring

import pytest

from lesson_3.exercise_5.is_hex import is_hex


@pytest.mark.parametrize("item, expected_result", [
    ("123", True),
    ("DEADBEEF", True),
    ("78AA", True),
    ("DUMMY", False),
    ("no hex", False),
])
def test_is_hex(item, expected_result):
    assert is_hex(item) == expected_result
