def odd_and_even(x:list[int]) -> list[int]:
    """Returns odd numbers at even indexes."""
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 1 and i % 2 == 0:
            x.append(x[i])
        i += 2
    return x
    