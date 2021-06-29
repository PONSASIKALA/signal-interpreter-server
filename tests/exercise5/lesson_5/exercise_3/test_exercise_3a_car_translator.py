# pylint: disable=missing-function-docstring

import pytest

from lesson_5.exercise_3.exercise_3a_car_translator import TranslatorFactory, SwedishTranslator, ItalianTranslator


class MockSwedishTranslator:
    def translate(self):
        pass


def test_swedish_translator():
    swedish_translator = SwedishTranslator()
    assert swedish_translator.get_car() == "bil"


def test_italian_translator():
    italian_translator = ItalianTranslator()
    assert italian_translator.get_car() == "macchina"


def test_register_language():
    translator_factory = TranslatorFactory()
    translator_factory.register_language("Swedish", MockSwedishTranslator)
    assert translator_factory._translators["Swedish"] == MockSwedishTranslator


def test_get_translator():
    translator_factory = TranslatorFactory()
    translator_factory._translators["Swedish"] = MockSwedishTranslator
    translator = translator_factory.get_translator("Swedish")
    assert translator == MockSwedishTranslator


def test_get_translator_with_invalid_language():
    translator_factory = TranslatorFactory()
    with pytest.raises(ValueError):
        translator_factory.get_translator("Norwegian")
