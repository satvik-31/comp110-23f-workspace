"""Combining two lists into a dictionary."""


__author__ = "730517765"

def zip(word: list[str], no: list[int])-> dict[str,int]:
    """Produce a dictionary where the keys are the items of the first list."""
    if len(word) != len(no):
        return {}
    if len(word) == 0 or len(no) == 0:
        return{}
    idx = 0 
    answer = {}
    while idx < len(word):
        answer[word[idx]] = no[idx]
        idx += 1
    return answer