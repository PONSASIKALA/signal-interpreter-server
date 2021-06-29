# pylint: disable=missing-function-docstring

class SwedishTranslator:
    def get_car(self):
        return "bil"


class ItalianTranslator:
    def get_car(self):
        return "macchina"


class TranslatorFactory:
    def __init__(self):
        self._translators = {}

    def register_language(self, language, translator):
        self._translators[language] = translator

    def get_translator(self, language):
        translator = self._translators.get(language)
        if not translator:
            raise ValueError(language)
        return translator


if __name__ == "__main__":
    language_from_user = input("Enter a language: ")

    translator_factory = TranslatorFactory()
    translator_factory.register_language("Swedish", SwedishTranslator)
    translator_factory.register_language("Italian", ItalianTranslator)

    fetched_translator = translator_factory.get_translator(language_from_user)
    car_in_other_language = fetched_translator().get_car()
    print(f"Car in {language_from_user} is {car_in_other_language}")
