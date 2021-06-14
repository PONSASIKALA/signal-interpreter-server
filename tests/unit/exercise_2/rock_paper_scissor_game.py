import random


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


def get_robot_choice():
    robot_choice = random.choice(["rock", "paper", "scissor"])
    print(f"Robot selected: {robot_choice}")
    return robot_choice


def play_game():
    player_choice = input("Select rock, paper or scissor: ")
    robot_choice = get_robot_choice()
    return decide_who_will_win(player_choice, robot_choice)


if __name__ == "__main__":
    print(play_game())
