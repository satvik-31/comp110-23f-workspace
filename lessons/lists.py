"""Practice with Lists"""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[0] = "cereal"

grocery_list[0] = "haha"
grocery_list.pop(1)
print(grocery_list)