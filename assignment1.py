# Name: Joshua Cicchinelli
# OSU Email: cicchinj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1
# Due Date: 1/27/26
# Description: Python Fundamentals Review - For this assignment, you will write a few short Python functions. 


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    Return the minimum and maximum values in the array.
    """

    min_val = arr[0]
    max_val = arr[0]

    # Loop through array
    for i in range(1, arr.length()):
        current = arr[i]
        # If i is smaller set it to minimum
        if current < min_val:
            min_val = current
        # If i is bigger set it to maximum
        elif current > max_val:
            max_val = current

    return min_val, max_val


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Returns an array with each element corresponding from StaticArray that is divisible by 3 being 'fizz', by 5 being 'buzz', by both 3 and 5 being 'fizzbuzz', and by none of those being the original value.
    """

    fizz_buzz_array = StaticArray(arr.length())

    # Iterates through each element
    for i in range (0, arr.length()):
        value = arr[i]
        # Divisible by 3 AND 5
        if value % 3 ==0 and value % 5 == 0:
            fizz_buzz_array[i] = "fizzbuzz"
        # Divisible by 3 
        elif value % 3 == 0:
            fizz_buzz_array[i] = "fizz"
        # Divisible by 5
        elif value % 5 == 0:
            fizz_buzz_array[i] = "buzz"
        # None of the Above, retruns original value
        else:
            fizz_buzz_array[i] = value
        
    return fizz_buzz_array


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverse the array in a given array
    """

    # Use 2 indexes: 1 for start, one for end
    left_index = 0
    right_index = arr.length() - 1

    # Swap values from outside moving towards the middle
    while left_index < right_index:
        temp = arr[left_index]
        arr[left_index] = arr[right_index]
        arr[right_index] = temp

        left_index += 1
        right_index -= 1




# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Return a new array rotated by the given number of steps.
    Positive rotates right, negative rotates left.
    """

    size = arr.length()
    rotated = StaticArray(size)

    # Sets rotation to absolute value and reduces steps
    shift = steps % size

    for i in range(size):
        # Move each value to new position
        new_index = (i + shift) % size
        rotated[new_index] = arr[i]

    return rotated


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Return a StaticArray containing all numbers from start to end.
    """
    
    #Figure out how many values we need and direction
    if start <= end:
        length = end - start + 1
        step = 1
    else:
        length = start - end + 1
        step = -1

    #create the result array
    result = StaticArray(length)
    current = start

    # Fill the new array 
    for i in range(length):
        result[i] = current
        current += step

    return result


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Return 1 if strictly ascending, -1 if strictly descending, 0 otherwise.
    """

    # Single element use-case
    if arr.length() == 1:
        return 1

    # Assume true
    ascending = True
    descending = True

    # Previous Value
    previous = arr[0]

    # Compare each element to the one before it
    for i in range(1, arr.length()):
        current = arr[i]

        # If current is not greater, it can't be asc
        if current <= previous:
            ascending = False
        # If current is not smaller it can't be strictly desc
        if current >= previous:
            descending = False
        # If neither, return 0
        if not ascending and not descending:
            return 0

        previous = current

    # Final result
    if ascending:
        return 1
    if descending:
        return -1
    return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------


def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Return the most frequent value and its count.
    """

    # Track most frequent value
    best_value = arr[0]
    best_count = 1

    # Track the current value and how many times it appears in a row
    current_value = arr[0]
    current_count = 1


    # Iterate through array
    for i in range(1, arr.length()):
        if arr[i] == current_value:
            # Same value as before, increase count
            current_count += 1
        else:
            # New value found, check if previous streak was the best
            if current_count > best_count:
                best_value = current_value
                best_count = current_count

            # Reset counters for the new value
            current_value = arr[i]
            current_count = 1

     # Final check in case the last value is the mode
    if current_count > best_count:
        best_value = current_value
        best_count = current_count

    return best_value, best_count


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Return a new array with duplicate values removed.
    """

    # Use-case for single value
    if arr.length() == 1:
        result = StaticArray(1)
        result[0] = arr[0]
        return result

    # First pass: count how many unique values there are
    unique_total = 1
    last_seen = arr[0]

    for i in range(1, arr.length()):
        if arr[i] != last_seen:
            unique_total += 1
            last_seen = arr[i]

     # Create the result array with the correct size
    result = StaticArray(unique_total)
    result[0] = arr[0]

    # Second pass: copy over only the unique values
    write_index = 1
    last_seen = arr[0]

    for i in range(1, arr.length()):
        if arr[i] != last_seen:
            result[write_index] = arr[i]
            write_index += 1
            last_seen = arr[i]

    return result


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    Sort the array in descending order using counting sort.
    """

    # Find the min and max values
    min_value = arr[0]
    max_value = arr[0]

    for i in range(1, arr.length()):
        if arr[i] < min_value:
            min_value = arr[i]
        elif arr[i] > max_value:
            max_value = arr[i]

     # Determine the size of the counting array
    range_size = max_value - min_value + 1
    counts = StaticArray(range_size)

    # Start at 0
    for i in range(range_size):
        counts[i] = 0

    # Count how many times each value appears
    for i in range(arr.length()):
        counts[arr[i] - min_value] += 1

    
    # Put in desc order
    result = StaticArray(arr.length())
    index = 0

    for offset in range(range_size - 1, -1, -1):
        value = min_value + offset
        for _ in range(counts[offset]):
            result[index] = value
            index += 1

    return result


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Return a new array containing the squares of each value, sorted.
    """

    size = arr.length()
    result = StaticArray(size)

    # Use two pointers, one at each end
    left = 0
    right = size - 1
    # Fill the result array from the back
    write_pos = size - 1

    while left <= right:
        left_sq = arr[left] * arr[left]
        right_sq = arr[right] * arr[right]

        # Place the larger square at the current write position
        if left_sq > right_sq:
            result[write_pos] = left_sq
            left += 1
        else:
            result[write_pos] = right_sq
            right -= 1

        write_pos -= 1

    return result


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result is not None and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-10 ** 9, 10 ** 9 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
