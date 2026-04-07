def find_and_replace(lst, find_val, replace_val):

    if not isinstance(lst, list):
        print("Error: The first argument must be a list.")
        return None

    modified_lst = []

    for item in lst:
        if item == find_val:
            modified_lst.append(replace_val)
        else:
            modified_lst.append(item)

    return modified_lst

original_list_1 = [1, 2, 3, 4, 2, 2]
print(f"Original List: {original_list_1}")
modified_list_1 = find_and_replace(original_list_1, 2, 5)
print(f"Modified List: {modified_list_1}")
print("-" * 30)

original_list_2 = ["apple", "banana", "apple"]
print(f"Original List: {original_list_2}")
modified_list_2 = find_and_replace(original_list_2, "apple", "orange")
print(f"Modified List: {modified_list_2}")
print("-" * 30)

print("--- Invoking find_and_replace('not a list', 1, 2) ---")
result_scenario_3 = find_and_replace("not a list", 1, 2)
print(f"Function returned: {result_scenario_3}")
print("-" * 30)
