import random


def get_three_heads():
    number_of_heads = 0
    number_of_tries = 0

    while number_of_heads < 3:
        heads_or_tails = random.choice(["heads", "tails"])
        print(f"Got {heads_or_tails}")
        if heads_or_tails == "heads":
            number_of_heads += 1
        number_of_tries += 1
    print(f"Number of tries until three heads: {number_of_tries}")


if __name__ == "__main__":
    get_three_heads()
