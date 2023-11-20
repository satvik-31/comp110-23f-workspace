"""File to define Fish class!"""


__author__ = "730517765"


class Fish:
    """Age attribute."""
    age: int

    def __init__(self):
        """Constructor for the fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Age tracker."""
        self.age += 1
        return None