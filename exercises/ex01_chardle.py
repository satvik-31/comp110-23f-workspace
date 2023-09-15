"""EX01 - Creating Chardle"""

__author__ = "730517765"

user_name: str = input("Enter a 5-character word: ")


if len(user_name) != 5:
    print("Error: Word must contain 5 characters")
    exit()
    
user_name_2: str = input("Enter a single character: ")

if len(user_name_2) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + user_name_2 + " in " + user_name)

number_of_instances: int = 0

if user_name_2 == user_name[0]:
    print(user_name_2 + str (" found at index 0 "))
    number_of_instances = number_of_instances + 1

if user_name_2 == user_name[1]:
    print(user_name_2 + str (" found at index 1 "))
    number_of_instances = number_of_instances + 1 

if user_name_2 == user_name[2]:
    print(user_name_2 + str (" found at index 2 "))
    number_of_instances = number_of_instances + 1

if user_name_2 == user_name[3]:
    print(user_name_2 + str (" found at index 3 "))
    number_of_instances = number_of_instances + 1

if user_name_2 == user_name[4]:
    print(user_name_2 + str (" found at index 4 "))
    number_of_instances = number_of_instances + 1

if number_of_instances == 1:
    print(str(number_of_instances) + " instance of " + user_name_2 + " found in " + user_name)
if number_of_instances > 1:
    print(str(number_of_instances) + " instances of " + user_name_2 + " found in " + user_name)
if number_of_instances == 0:
    print( "No instances of " + user_name_2 + " found in " + user_name)



