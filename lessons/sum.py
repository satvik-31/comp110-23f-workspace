"""Summing the elements of a list using different loops."""

__author__: str = "730517765"


def w_sum(vals: list[float]) -> float:
    """Returs the sum of the three floats using a while loop."""
    idx: int = 0 
    result: float = 0.0
    while idx < len(vals): 
        result += vals[idx] 
        idx += 1 
    return result


def f_sum(vals: list[float]) -> float:
    """Returns the sum of three floats in a list using for...in loops."""
    count: float = 0.0
    for i in vals:
        count += i
    return count


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of three floats in a list using for...in...range loops."""
    sand: float = 0
    for i in range(len(vals)):
        sand += vals[i]
    return sand