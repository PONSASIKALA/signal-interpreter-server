# pylint: disable=missing-function-docstring

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_display_word(secret_word):
    display_word = []
    for i in range(len(secret_word)):
        if secret_word[i] in ALPHABET:
            display_word.append("_")
        else:
            display_word.append(secret_word[i])
    return display_word


def get_valid_guess():
    input_is_invalid = True
    guess = None
    while input_is_invalid:
        guess = input("Player 2, please guess a letter: ").upper()
        if len(guess) > 1 or guess not in ALPHABET:
            print("You did not enter a valid guess. Please try again.")
        else:
            input_is_invalid = False
    return guess


def set_display_word(guess, secret_word, display_word):
    for i, letter in enumerate(secret_word):
        if letter == guess:
            display_word[i] = guess
    return display_word


def print_display_word(display_word):
    word = ""
    for i in range(len(display_word)):
        word += display_word[i]
    print()
    print("Current Progress: ", word)


def play_hangman(secret_word):
    guesses_left = 6
    display_word = get_display_word(secret_word)

    while '_' in display_word and guesses_left:
        guess = get_valid_guess()
        if guess in secret_word:
            display_word = set_display_word(guess, secret_word, display_word)
        else:
            print("Your guess is incorrect! Please try again.")
            guesses_left -= 1
            print(f"Number of guesses left: {guesses_left}")

        print_display_word(display_word)

    if "_" not in display_word:
        print("Player 2 wins!")
    else:
        print("You died!")


def initialize_game():
    secret_word = input("Player one, please enter your secret word: ").upper()
    for i in range(50):
        print()
    print("Player two must guess Player one's word")
    play_hangman(secret_word)


initialize_game()
