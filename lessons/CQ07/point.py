"""Creating a class."""


from __future__ import annotations


__author__ = "730517765"


class Point:
    """Creating points."""
    x: float
    y: float 

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Creating floats as positional coordinates."""
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
    
    def __str__(self) -> str:
        """Method to print out points in a readable way."""
        result: str = f"x: {self.x}; y: {self.y}"
        return result
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplies previous points with a factor."""
        new_pointx = self.x * factor 
        new_pointy = self.y * factor 
        return Point(new_pointx, new_pointy)
    
    def __add__(self, factor: int | float) -> Point:
        """Overloads the addition operator."""
        new_pointx = self.x + factor 
        new_pointy = self.y + factor 
        return Point(new_pointx, new_pointy)


my_point: Point = Point()
print(my_point)