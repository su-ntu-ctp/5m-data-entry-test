def update_dictionary(dct, key, value):

    if key in dct:
        print(f"Key '{key}' already exists. Original value was: {dct[key]}")    
    dct[key] = value    
    return dct

empty_dict = {}
print("--- Scenario 1: Adding a new key ---")
print(f"Original dictionary: {empty_dict}")
updated_dict_1 = update_dictionary(empty_dict, "name", "Alice")
print(f"Updated dictionary: {updated_dict_1}")
print("-" * 30)

existing_dict = {"age": 25}
print("--- Scenario 2: Updating an existing key ---")
print(f"Original dictionary: {existing_dict}")
updated_dict_2 = update_dictionary(existing_dict, "age", 26)
print(f"Updated dictionary: {updated_dict_2}")
print("-" * 30)
