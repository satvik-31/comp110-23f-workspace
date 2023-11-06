"""Practicing writing functions in different ways."""

def w_sum(vals: list[float]) -> float:
    """Returns the sum of the elemets in the list using "while" loops."""
    i: int = 0 
    sum: float = 0.0
    while i < len(vals):
        if vals == ([]):
            return sum
        else:
            sum = sum + vals[i]
        i += 1
    return sum


def f_sum(summing: list[float]) -> float:
    """Returns sum using for..in..loops"""
    result: float = 0.0
    for elem in summing: 
        result = result + elem
    return result


def f_range_sum(vals: list[float]) -> float:
    """Returns sum using for in range loops."""
    total: float = 0.0
    for each in range(len(vals)):
        total = total + vals[each]
    return total

