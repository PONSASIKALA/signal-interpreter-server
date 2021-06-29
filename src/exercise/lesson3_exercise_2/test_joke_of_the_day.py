# pylint: disable=missing-function-docstring

from unittest.mock import patch, call

from lesson_3.exercise_2.joke_of_the_day import joke_of_the_day


@patch("builtins.print")
def test_joke_of_the_day_wrong_answer(mock_print):
    with patch("builtins.input", return_value="Do not know"):
        joke_of_the_day()
        assert mock_print.mock_calls == [call("--- Joke of the day ---"),
                                         call("Wrong answer! The correct answer is 'Roberto!'")]


@patch("builtins.print")
def test_joke_of_the_day_correct_answer(mock_print):
    with patch("builtins.input", return_value="Roberto"):
        joke_of_the_day()
        assert mock_print.mock_calls == [call("--- Joke of the day ---"),
                                         call("Correct!")]
