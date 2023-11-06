"""Testing EX06 Dictionary Functions."""


__author__ = "730517765"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

#Use cases
def test_invert():
    """Tests for invert of keys and values."""
    x = {"From" : "4", "Grape" : "5"}
    flipped_list = {"4" : "From", "5": "Grape"}
    answer = invert(x)
    assert answer == flipped_list

def test_invert1():
    """Inverting the keys and the values!"""
    x = {"Spider" : "8", "Humans" : "2", "Elephants" : "Four"}
    y = invert(x)
    assert y

#Edge Case - Invert 
def test_invert2():
    """Inverts the keys and values!"""
    x = {}
    y = invert(x)
    assert y == {}

# Use cases - Favorite Color
def test_favcolor():
    """Returns the color that appeasr most frequently as a string."""
    y = {"Sky" : "Blue", "Water" : "Blue", "Sun" : "Yellow", "Grass" : "Green"}
    assert favorite_color(y) == ("Blue")


def test_color():
    """Returns the color that appears most frequently."""
    y = {"Orange" : "Orange", "Banana" : "Yellow", "Jackfruit" : "Yellow", "Strawberry" : "Red", "Watermelon" : "Green"}
    assert favorite_color(y) == ("Yellow")

# Edge cases - Favorite Color
def test_mostcolor():
    """Returns an empty string due to empty input!"""
    y = {}
    assert favorite_color(y) == ("")





