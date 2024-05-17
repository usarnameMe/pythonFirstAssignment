def convert_fun(input_value):
    if isinstance(input_value, str):
        try:
            return int(input_value)
        except ValueError:
            return "Oh no, you cannot convert string to integer."
    elif isinstance(input_value, int):
        return str(input_value)
    else:
        return "Error: This type is not supported! Try another one!"


user_input = input("Enter a value: ")

try:
    user_input = int(user_input)
except ValueError:
    pass

converted_value = convert_fun(user_input)
print(f"Converted value: {converted_value}")
