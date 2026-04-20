def swap(x, y):

    if isinstance(x, (int, float)) and isinstance(y, (int, float)):

        x = x + y
        y = x - y
        x = x - y
        print(f"The swapped values are: x = {x}, y = {y}")
   
    else:

        print("Error: Both x and y must be numeric values.")
        return -1

print("--- Invoking swap('Apple', 10) ---")
result_scenario_1 = swap("Apple", 10)
print(f"Function returned: {result_scenario_1}")
print("-" * 30)

print("--- Invoking swap(9, 17) ---")
result_scenario_2 = swap(9, 17)
print(f"Function returned: {result_scenario_2}")
print("-" * 30)
