"""Defining the Pizza class for practice."""

from __future__ import annotations 

class Pizza:
    size: str 
    toppings: int 
    gluten_free: bool

    def __init__(self,size: str, toppings: int, gluten_free: bool):
        self.size = size
        self.toppings = toppings
        self.gluten_free = gluten_free

    # Method Price 
    def add_toppings(self,num_toppings: int):
        self.toppings += num_toppings

# Function price 
def price(input: Pizza) -> float: 
    if input.gluten_free:
        price: float = 8.00
    else:
        price: float = 5.00
    price += 1.00 * input.toppings
    return price


my_pizza: Pizza = Pizza("tiny", 4, False)
print(my_pizza)

sals_pizza: Pizza = Pizza("medium", 5, False)

print(price(sals_pizza))
my_pizza.add_toppings(2)
print(my_pizza.toppings)

