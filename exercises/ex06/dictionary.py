"""Practicing dictionary functions!"""


__author__ = "730517765"


# Keys are unique, raise a 'KeyError' when they are repeated.
def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values!"""
    dict_inv: dict[str, str] = {}
    for key in x:
        if x[key] in dict_inv:
            raise KeyError("Error: More than one of the same key!")
        value = x[key]
        dict_inv[value] = key
    return dict_inv


def favorite_color(y: dict[str, str]) -> str:
    """Returns color that appears most frequently."""
    colour_app: str = ""
    dict_colour: dict[str, int] = {}
    no_colour: int = 0
# for loop that checks each element 
    for elem in y:
        most_freq = y[elem]
        if most_freq in dict_colour:
            dict_colour[most_freq] += 1
        else:
            dict_colour[most_freq] = 1
    
    for colour in dict_colour: 
        freq: int = dict_colour[colour]
        if no_colour < freq:
            no_colour = freq
            colour_app = colour
    return colour_app


def count(list_of_stuff: list[str]) -> dict[str, int]:
    """Returns the number of times a value is mentioned in the list."""
    empty_dict: dict[str, int] = {}
    for key in list_of_stuff:
        if key in empty_dict:
            empty_dict[key] += 1
        else:
            empty_dict[key] = 1
    return empty_dict


def alphabetizer(categorize: list[str]) -> dict[str, list[str]]:
    """Returns keys with a letter and values with words that start with that letter."""
    empty_dict: dict[str, list[str]] = {}
    for elem in categorize:
        let = elem[0].lower()

        if let in empty_dict:
            empty_dict[let].append(elem)
        else:
            empty_dict[let] = [elem]
    return empty_dict


def update_attendance(exist: dict[str, list[str]], day: str, stud: str) -> dict[str, list[str]]:
    """Mutate and return dictionary with days as keys and students in attendance as values."""
    if day in exist:
        if stud not in exist[day]:
            exist[day].append(stud)

    else:
        exist[day] = [stud]
    return exist