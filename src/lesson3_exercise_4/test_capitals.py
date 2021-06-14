import pytest

from lesson_3.exercise_4.capitals import practice_capitals


from unittest.mock import patch


@patch("lesson_3.exercise_4.capitals.get_capital", return_value="Stockholm")
@patch("builtins.print")
@patch("builtins.input", side_effect=["Sweden"])
def test_practice_capitals_with_valid_country(mock_input, mock_print, mock_get_capital):
	practice_capitals()
	mock_get_capital.assert_called_with("Sweden")
	mock_print.assert_called_with("The capital of Sweden is Stockholm")


@patch("lesson_3.exercise_4.capitals.get_capital", side_effect=KeyError)
@patch("builtins.print")
@patch("builtins.input", side_effect=["DummyCountry"])
def test_practice_capitals_with_invalid_country(mock_input, mock_print, mock_get_capital):
	practice_capitals()
	mock_get_capital.assert_called_with("DummyCountry")
	mock_print.assert_called_with("DummyCountry does not exist in our dictionary")
