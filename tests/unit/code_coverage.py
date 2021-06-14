def code_coverage(input_value):
    try:
        int(input_value, 16)
        return True
    except ValueError:
        return False
