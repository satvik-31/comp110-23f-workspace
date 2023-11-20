"""Challenge Question Class."""

from __future__ import annotations
 
 
class Point:
    """Class to represent (x,y) coordinate point."""
    
    x: float
    y: float
    
    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Construct a point."""
        self.x = init_x
        self.y = init_y
    
    def scale_by(self, factor: int) -> None:
        """Modify (or mutate) a point."""
        self.x *= factor
        self.y *= factor
        
    def scale(self, factor: int) -> Point:
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Prints the result of the attributes."""
        result: str = f"x: {self.x}, y: {self.y}"
        return result
    
    def __mul__(self, factor: int | float):
        """Multiplication overload."""
        new_x = self.x * factor 
        new_y = self.y * factor
        return Point(new_x, new_y)
    
    def __add__(self, factor: int | float):
        """Adds to the coordinates."""
        new_x = self.x + factor 
        new_y = self.y + factor
        return Point(new_x, new_y)


# Calling the functions to check if they are defined properly 

testingdefaultpara: Point = Point()
print(testingdefaultpara)


my_point: Point = Point(1.0, 2.0)
print(str(my_point))
newpoint: Point = my_point * 7
print(newpoint)
addpoint: Point = newpoint + 2.0
print(addpoint)

