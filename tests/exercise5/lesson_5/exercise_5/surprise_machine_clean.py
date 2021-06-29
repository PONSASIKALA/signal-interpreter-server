# pylint: disable=missing-function-docstring

import random
import time


def surprise_machine():
    random_number = random.randint(0, 10)
    time.sleep(random_number)
    print("Surprise!!!")


if __name__ == "__main__":
    surprise_machine()
