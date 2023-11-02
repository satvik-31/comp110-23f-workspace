"""Practicing directory functins!"""

__author__ = "730517765"

#Keys are unique, raise a 'KeyError' when they are repeated.
def invert(x: dict[str,str])-> dict[str,str]:
    """Inverts the keys and the values!"""
    inverted_dict: {}
    for elem in x:
        value = x[elem]
        inverted_dict[value] = elem
    return inverted_dict
i

def favorite_color(y: dict[str,str]) -> str:
    """Returns color that appears most frequently."""
    colour_app: str = ""
    dict_colour = {}
#for loop that checks each element 
    for elem in y:
#Return the values that appear the most number of times
        most_freq = y[elem]
        if most_freq in colour_app:
            most_freq += 1
            return True 
        else:
            most_freq = 1
    
    for colour in dict_colour:
        no_colour: int = 0 
        freq: int = dict_colour[colour]
        if no_colour < freq:
            no_colour = freq
            colour_app = colour
    return colour_app
