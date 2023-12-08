def free_biscuits(games: dict[str, list[int]]) -> dict[str, bool]:
    """x."""
    j: int = 0 
    result: int = 0 
    new_dict: dict[str, bool] = {}
    for i in games:
        point: list[int] = games[i]
        while j < len(point):
            result += point[j]
            j += 1
        if result >= 100:
            new_dict[i] = True 
        else:
            new_dict[i] = False
    return new_dict

x = free_biscuits({"UNCvsDuke": [38, 20, 42], "“UNCvsState": [4, 51, 16, 23]})
print(x)

def reverse_multiply(input: list[int]) -> list[int]:
    """c."""
    new_list: list[int] = []
    i = (len(input) - 1)
    while i >= 0:
        result = (input[i] * 2)
        new_list.append(result)
        i -= 1
    return new_list

y = reverse_multiply([1,2,3,4])
print(y)


