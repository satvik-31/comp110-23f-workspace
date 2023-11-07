"""Testing EX06 Dictionary Functions."""


__author__ = "730517765"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Use cases - Invert
def test_invert():
    """Tests for invert of keys and values."""
    x = {"From": "4", "Grape": "5"}
    flipped_list = {"4": "From", "5": "Grape"}
    answer = invert(x)
    assert answer == flipped_list


def test_invert1():
    """Inverting the keys and the values!"""
    x = {"Spider": "8", "Humans": "2", "Elephants": "4"}
    y = invert(x)
    assert y


#Edge Case - Invert 
def test_invert2():
    """Inverts the keys and values!"""
    x = {}
    y = invert(x)
    assert y == {}


# Use cases - Favorite Color
def test_favcolor():
    """Returns the color that appeasr most frequently as a string."""
    y = {"Sky": "Blue", "Water": "Blue", "Sun": "Yellow", "Grass": "Green"}
    assert favorite_color(y) == ("Blue")


def test_color():
    """Returns the color that appears most frequently."""
    y = {"Orange": "Orange", "Banana": "Yellow", "Jackfruit": "Yellow", "Strawberry": "Red", "Watermelon": "Green"}
    assert favorite_color(y) == ("Yellow")


# Edge case - Favorite Color
def test_mostcolor():
    """Returns an empty string due to empty input!"""
    y = {}
    assert favorite_color(y) == ("")


# Use cases - Count
def test_counter():
    """Returns the frequency of an item appearing in a list."""
    list_of_stuff: list[str] = ["Ben", "Ten", "Ben", "Franklin", "Ben", "Kingsley"]
    assert count(list_of_stuff) == {"Ben": 3, "Ten": 1, "Franklin" : 1, "Kingsley" : 1}


def test_counter2() :
    """Returns the frequency of an item appearing in a list."""
    list_of_stuff: list[str] = ["Thor", "Iron Man", "Batman", "Superman", "Winter Soldier", "Mandarin"]
    assert count(list_of_stuff) == {"Thor": 1, "Iron Man": 1, "Batman" : 1, "Superman" : 1, "Winter Soldier" : 1, "Mandarin" : 1}


# Edge Case - Count
def test_counter3() :
    """Returns an empty dictionary when an empty list is input."""
    list_of_stuff: list[str] = []
    assert count(list_of_stuff) == {}


# Use Case - Alphabetizer 
def test_alpha():
    """Returns keys with a letter and values as words beginning with that letter."""
    categorize: list[str] = ["Bio", "Bronco", "Dinosaur", "Destiny"]
    assert alphabetizer(categorize) == {"b" : ["Bio", "Bronco"], "d": ["Dinosaur", "Destiny"]}


def test_alpha2():
    """Returns keys with a letter and values as words beginning with that letter."""
    categorize: list[str] = ["Burt", "Brynn", "Dali", "Dame", "Grodd", "Baird",]
    assert alphabetizer(categorize) == {"b" : ["Burt", "Brynn", "Baird"], "d": ["Dali", "Dame"],"g": ["Grodd"]}


# Edge Case - Alphabetizer 
def test_alpha3():
    """Returns empty dictionary when input is an empty list."""
    categord: list[str] = []
    assert alphabetizer(categord) == {}


# Use Case - Update_Attendance
def test_attend():
    """Returns days as keys and students in attendance as values."""
    exist: dict[str, list[str]] = {"Monday": ["George", "Mandy", "Sunny"], "Tuesday" : ["Sunny"]}
    day: str = "Monday"
    stud: str = "George"
    assert update_attendance(exist, day, stud) == {"Monday", ["George", "Mandy"]}




