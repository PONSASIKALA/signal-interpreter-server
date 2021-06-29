# pylint: disable=missing-function-docstring

from unittest.mock import patch

import pytest

from lesson_5.exercise_2.exercise_2a_car_translator import SwedishTranslator, ItalianTranslator, translate_car


def test_swedish_translator():
    swedish_translator = SwedishTranslator()
    assert swedish_translator.get_car() == "bil"


def test_italian_translator():
    italian_translator = ItalianTranslator()
    assert italian_translator.get_car() == "macchina"


def test_translate_car_with_swedish_language():
    with patch.object(SwedishTranslator, "get_car") as mock_translate_car_to_swedish:
        translate_car("Swedish")
        mock_translate_car_to_swedish.assert_called_once()


def test_translate_car_with_italian_language():
    with patch.object(ItalianTranslator, "get_car") as mock_translate_car_to_italian:
        translate_car("Italian")
        mock_translate_car_to_italian.assert_called_once()


def test_translate_car_with_invalid_language():
    with pytest.raises(ValueError):
        translate_car("Norwegian")
