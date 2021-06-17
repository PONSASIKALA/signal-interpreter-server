from lesson_2.exercise_3.get_name_from_user import get_name_from_user


def get_welcome_message():
    name = get_name_from_user()
    welcome_message = f"Welcome {name}!"
    return welcome_message
