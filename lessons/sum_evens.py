"""Practicing summing over lists."""

def sum_check(x: list[int]) -> int:
    """Sum all even numbers in the list."""
    idx: int = 0
    sum: int = 0
    while idx < len(x):
        number: int = x[idx]
        if number % 2 == 0:
            sum = sum + number
        idx += 1
    return sum

def sum_evens_in_list(input_list: list[int]) -> int:
    """Sum all even numbers in this list."""
    list_sum: int = 0
    for elem in input_list:
        if elem % 2 == 0: 
            list_sum = list_sum + elem
    return list_sum