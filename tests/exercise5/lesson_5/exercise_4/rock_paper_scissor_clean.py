# pylint: disable=missing-function-docstring

import random

options = ["rock", "paper", "scissor"]


def decide_who_will_win(player_hand, robot_hand):
    if player_hand == "rock" and robot_hand == "scissor":
        print("You won!")
    elif player_hand == "paper" and robot_hand == "rock":
        print("You won!")
    elif player_hand == "scissor" and robot_hand == "paper":
        print("You won!")
    elif player_hand == robot_hand:
        print("It was a tie.")
    else:
        print("You lost.")


for i in range(0, 3):
    player_choice = input("Select rock, paper or scissor: ")
    random_index = random.randint(0, 2)
    robot_choice = options[random_index]
    print(f"Robot selected: {robot_choice}")
    decide_who_will_win(player_choice, robot_choice)
