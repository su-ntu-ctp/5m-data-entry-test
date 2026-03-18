def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x, y = y, x  
    print(f"Swapped: x={x}, y={y}")
    return
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple", 10)  # Returns -1 (non-numeric)
swap(9, 17)        # Prints: Swapped: x=17, y=9
