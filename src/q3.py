def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    # Update the dictionary with the new value
    dct[key] = value
    
    # Return the updated dictionary
    return dct

    Task 2
    # Scenario 1: {}, "name", "Alice"
print(update_dictionary({}, "name", "Alice"))  # Output: {"name": "Alice"}

# Scenario 2: {"age": 25}, "age", 26
print(update_dictionary({"age": 25}, "age", 26))  # Output: prints "Original value for 'age': 25" and returns {"age": 26}
