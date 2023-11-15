"""Instantiating a class."""

from lessons.classes.pizza import Pizza


# You are essentially creating your own type 
my_pizza: Pizza = Pizza("large", 10, True) #CONSTRUCTOR

# accessing the attributes 
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

# printing out my pizza

print(f"my_pizza: {my_pizza}")

print(f"pizza: {Pizza}")

print(f"Size attribute: {my_pizza.size}")

sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float: 
    """Function of Price of pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    
    else:
        price: float = 5.00
    price = price + .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00 
    return price

print(price(sals_pizza))
print(price(my_pizza))

print(sals_pizza.price())
print(my_pizza.price())

# Calling a method 
my_pizza.price()

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_new_toppings(2)
print(my_other_pizza.toppings)