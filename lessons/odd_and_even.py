def odd_and_even(x:list[int]) -> list[int]:
    """Returns odd numbers at even indexes."""
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 1 and i % 2 == 0:
            x.append(x[i])
        i += 2
    return x

def value_exists(x: dict[str,int], y: int) -> bool:
    """Return."""
    for elem in x:
        if y == x[elem]:
            return True
    else:
        return False
    

def short_words(x:list[str]) -> list[str]:
    """Retunr."""
    i: int = 0
    result =[]
    for i in range  (0, len(x)):
        if len(x[i]) < 5:
            result.append(x[i])
        else:
            print (f"{x[i]} was too long")
        i += 1
    return result
