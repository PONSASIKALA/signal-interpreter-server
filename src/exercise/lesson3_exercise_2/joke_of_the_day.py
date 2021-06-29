def joke_of_the_day():
    print("--- Joke of the day ---")
    answer = input("What do you call a man with a rubber toe? ")
    if 'roberto' in answer.lower():
        print("Correct!")
    else:
        print("Wrong answer! The correct answer is 'Roberto!'")


if __name__ == "__main__":
    joke_of_the_day()
