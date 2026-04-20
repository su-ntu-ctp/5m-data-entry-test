def string_reverse(s):

    if not isinstance(s, str):
        print("Error: The input must be a string.")
        return None

    return s[::-1]

string_1 = "Hello World"
print(f"Original string: '{string_1}'")
reversed_string_1 = string_reverse(string_1)
print(f"Reversed string: '{reversed_string_1}'")
print("-" * 30)

string_2 = "Python"
print(f"Original string: '{string_2}'")
reversed_string_2 = string_reverse(string_2)
print(f"Reversed string: '{reversed_string_2}'")
print("-")
