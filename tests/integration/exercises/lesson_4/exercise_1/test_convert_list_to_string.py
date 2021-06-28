from lesson_4.exercise_1.convert_list_to_string import convert_to_comma_separated_string, \
    convert_to_space_separated_string


def test_convert_to_comma_separated_string(test_list):
    assert convert_to_comma_separated_string(test_list) == "one,two,three"


def test_convert_to_space_separated_string(test_list):
    assert convert_to_space_separated_string(test_list) == "one two three"
