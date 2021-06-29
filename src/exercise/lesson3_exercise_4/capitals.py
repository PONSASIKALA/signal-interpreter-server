# pylint: disable=missing-function-docstring

def practice_capitals():
    country = input("Enter a country: ")
    try:
        capital = get_capital(country)
        print(f"The capital of {country} is {capital}")
    except KeyError:
        print(f"{country} does not exist in our dictionary")


def get_capital(country):
    country_capital_dictionary = {"Sweden": "Stockholm",
                                  "Italy": "Rome",
                                  "United Kingdom": "London",
                                  "Norway": "Oslo",
                                  "Japan": "Tokyo"}
    return country_capital_dictionary[country]


if __name__ == "__main__":
    practice_capitals()
