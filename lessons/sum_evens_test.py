"""Testing my summaation function."""

from lessons.sum_evens import sum_evens_in_list

def test_empty_sum() -> None:
    """Sum evens in list of empty list should be 0."""
    assert sum_evens_in_list([]) == 0

def test_list_length_1():
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sum_evens_in_list(test_list) == 2

from lessons.sum_evens import sum_check

def test_sum_even():
    """Tests sum of all even numbers in list."""
    x: list[int] = ([1,2,3,4,5,6])
    assert sum_check(x) == 12