"""Creating a class."""


from __future__ import annotations


__author__ = "730517765"


class Point: 
    x: float
    y: float 


    def __init__(self, x_init: float, y_init: float) -> None:
        self.x = x_init
        self.y = y_init

    
    def scale_by(self, factor: int) -> None:
        """Method that updates the x and y attributes."""
        self.x *= factor
        self.y *= factor

    
    def scale(self, factor: int) -> Point:
        """Return a new point after mutating the values of x and y."""
        true_x = self.x * factor 
        true_y = self.y * factor
        return Point(true_x, true_y)