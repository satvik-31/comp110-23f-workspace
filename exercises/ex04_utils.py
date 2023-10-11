"""Utils!"""

___author__: str = "730517765"


def all(options: list[int], the_one: int) -> bool:
    """Finds if every number in the list is equal to one outside!"""
    idx: int = 0
    while idx < len(options):
        if the_one == options[idx]:
            idx = idx + 1  
        else: 
            return False
    if len(options) == 0:
        return False
    return True
        

def max(large: list[int])-> int:
    """Given a list of functions, returns the largest value!"""
    if len(large) == 0:
        raise ValueError("max() arg is an empty List")
# Use the same logic as the "current_card" and "lowest_card" example from class
    indx: int = 0
    big = large[0]
    while indx < len(large):
        if big < large[indx]:
            big = large[indx]
        indx += 1
    return big


def is_equal(list1: list[int], list2: list[int])-> bool:
    """Checks if the two lists are equal to each other!"""
    ildx: int = 0
    total: int = 0 
    if len(list1) > len(list2):
        small = list2
    else:
        small = list1

    while ildx < len(small):
        if list1[ildx] == list2[ildx]:
            ildx += 1
            total += 1
        else: 
            ildx += 1
    if (total == len(small)) and len(list1) == len(list2):
        return True
    return False
