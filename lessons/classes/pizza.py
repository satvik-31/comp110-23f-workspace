"""Defining a class."""

from __future__ import annotations


class Pizza:
    #attributes 
    size: str
    toppings: int
    gluten_free: bool

# here self is taken as an argument 
# self is always first argument 
    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf

    # Method is defined inside a class function

    def price(self) -> float:
        """Method of Price of pizza."""
        if self.size == "large":
            price: float = 6.25
        
        else:
            price: float = 5.00
        price = price + .75 * self.toppings
        if self.gluten_free:
            price += 1.00 
        return price

 