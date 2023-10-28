"""Test my zip function."""

__author__ = "730517765"

from lessons.zip import zip


def jordan() -> None:
    word = ["january", "february"]
    no = [1]
    jordan = zip(word, no)
    assert jordan == {}

def zip_test() -> None:
    """Tests list to dictionary conversion"""
    word = ["Dragon", "Bane", "Caramel"]
    no = [1, 2, 3]
    result = {"Dragon": 1, "Bane": 2, "Caramel": 3}
    jordan = zip(word, no)
    assert result == jordan

