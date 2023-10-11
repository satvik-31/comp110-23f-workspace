"""Practicing Counters"""

#Initialize the string I want to count thee odds of
num_string: str = "103"
#Initialize my counter for number of odds
num_of_odds: int = 0
x: int = 0

while len(num_string) > num_of_odds:
    if int(num_string[x]) % 2 == 1:
     num_of_odds = num_of_odds + 1
x += 1
print(num_of_odds)
    