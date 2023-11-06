"""Test my zip function."""


__author__ = "730517765"

from lessons.zip import zip


def test_jordan() -> None:
    """Testing the call."""
    word = ["january", "february"]
    no = [1]
    jordan = zip(word, no)
    assert jordan == {}

def test_zip() -> None:
    """Tests list to dictionary conversion."""
    word = ["Dragon", "Bane", "Caramel"]
    no = [1, 2, 3]
    result = {"Dragon": 1, "Bane": 2, "Caramel": 3}
    jordan = zip(word, no)
    assert result == jordan

def test_zip2() -> None:
    """Tests list to dictionary conversion."""
    word = ["Cupboard", "Table", "Chair"]
    no = [1, 2, 3]
    troll = {"Cupboard": 1, "Table": 2, "Chair": 3}
    jordan = zip(word, no)
    assert troll == jordan
