# pylint: disable=missing-function-docstring

from unittest.mock import patch

from lesson_5.exercise_5.surprise_machine_clean import surprise_machine


def test_surprise_machine():
    with patch("builtins.print") as mock_print:
        with patch("lesson_5.exercise_5.surprise_machine_clean.random.randint", return_value=4):
            with patch("lesson_5.exercise_5.surprise_machine_clean.time.sleep") as mock_sleep:
                surprise_machine()
                mock_sleep.assert_called_with(4)
                mock_print.assert_called_with("Surprise!!!")
