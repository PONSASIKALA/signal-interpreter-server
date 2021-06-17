from unittest.mock import patch

from lesson_2.exercise_2.rock_paper_scissor_game import decide_who_will_win, get_robot_choice, play_game


def test_decide_who_will_win():
    assert decide_who_will_win("rock", "scissor") == "You won!"
    assert decide_who_will_win("scissor", "paper") == "You won!"
    assert decide_who_will_win("paper", "rock") == "You won!"
    assert decide_who_will_win("scissor", "rock") == "You lost."
    assert decide_who_will_win("paper", "scissor") == "You lost."
    assert decide_who_will_win("rock", "paper") == "You lost."
    assert decide_who_will_win("rock", "rock") == "It was a tie."
    assert decide_who_will_win("scissor", "scissor") == "It was a tie."
    assert decide_who_will_win("paper", "paper") == "It was a tie."


def test_get_robot_choice():
    with patch("lesson_2.exercise_2.rock_paper_scissor_game.random.choice") as mock_choice:
        mock_choice.return_value = "scissor"
        assert get_robot_choice() == "scissor"


def test_play_game():
    with patch("builtins.input", return_value="rock"):
        with patch("lesson_2.exercise_2.rock_paper_scissor_game.get_robot_choice", return_value="scissor"):
            with patch("lesson_2.exercise_2.rock_paper_scissor_game.decide_who_will_win", return_value="You won!"):
                assert play_game() == "You won!"
