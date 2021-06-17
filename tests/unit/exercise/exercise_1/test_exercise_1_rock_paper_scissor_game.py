from lesson_2.exercise_1.rock_paper_scissor_game import decide_who_will_win


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
