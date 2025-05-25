def validate_number(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid number input")
