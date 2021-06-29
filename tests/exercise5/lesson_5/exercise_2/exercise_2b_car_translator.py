# pylint: disable=missing-function-docstring

class SwedishTranslator:
    def get_car(self):
        return "bil"


class ItalianTranslator:
    def get_car(self):
        return "macchina"


class GermanTranslator:
    def get_car(self):
        return "auto"


def translate_car(language):
    if language == "Swedish":
        swedish_translator = SwedishTranslator()
        return swedish_translator.get_car()
    elif language == "Italian":
        italian_translator = ItalianTranslator()
        return italian_translator.get_car()
    elif language == "German":
        german_translator = GermanTranslator()
        return german_translator.get_car()
    else:
        raise ValueError(f"{language} is not supported")


if __name__ == "__main__":
    language_from_user = input("Enter a language: ")
    car_in_other_language = translate_car(language_from_user)
    print(f"Car in {language_from_user} is {car_in_other_language}")
