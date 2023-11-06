"""Calling Zip functions - CQ06!"""

from lessons.zip import zip

def test_zip():
    """Checks if dictionary is produced with keys as items from first list."""
    word = (["jack", "chrome", "dome"])
    no = ([1,2,3])
    answer = {"jack": 1, "chrome": 2, "dome" : 3}
    assert zip(word, no) == answer