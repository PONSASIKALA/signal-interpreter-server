def decide_who_will_win(player_hand, robot_hand):
    if player_hand == "rock" and robot_hand == "scissor":
        return "You won!"
    elif player_hand == "paper" and robot_hand == "rock":
        return "You won!"
    elif player_hand == "scissor" and robot_hand == "paper":
        return "You won!"
    elif player_hand == robot_hand:
        return "It was a tie."
    else:
        return "You lost."
