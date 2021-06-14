from unittest.mock import patch

from lesson_3.exercise_1.main import main, init


def test_main():
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_with("Hello world!")


def test_init():
    with patch("lesson_3.exercise_1.main.main") as mock_main:
        with patch("lesson_3.exercise_1.main.__name__", "__main__"):
            init()
            mock_main.assert_called_once()
