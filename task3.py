if __name__ == '__main__':
    # Convert an integer to a floating-point number
    integer_value = 10
    float_value = float(integer_value)

    print("Integer:", integer_value)
    print("Converted to float:", float_value)
    print("Type:", type(float_value))

    # Convert a floating-point number to an integer
    float_number = 10.5
    integer_number = int(float_number)

    print("\nFloat:", float_number)
    print("Converted to integer:", integer_number)
    print("Type:", type(integer_number))

    # Convert an integer to a string
    number = 100
    string_number = str(number)

    print("\nInteger:", number)
    print("Converted to string:", string_number)
    print("Type:", type(string_number))

    # Convert a string containing a number to an integer
    string_value = "50"
    converted_integer = int(string_value)

    print("\nString:", string_value)
    print("Converted to integer:", converted_integer)
    print("Type:", type(converted_integer))

    # Convert an integer to a Boolean
    integer_boolean = 1
    boolean_value = bool(integer_boolean)

    print("\nInteger:", integer_boolean)
    print("Converted to Boolean:", boolean_value)
    print("Type:", type(boolean_value))