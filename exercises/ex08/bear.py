"""Fisle to define Bear class!"""

__author__ = "730517765"


class Bear:
    """Attributes."""
    age: int
    hunger_score: int

    def __init__(self):
        """Constructor for the Bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Age and Hunger counter."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Fish eaten tracker."""
        self.hunger_score += num_fish
        return None