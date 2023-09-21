"""Running One-Shot-Wordle!"""

__author__ = "730517765"

#
user_name = input("What is your 6 letter guess? ")
secret_word: str = "python"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

# You cannot mention it as greater than or less than 6 as the program must work for any length 
while len(user_name) != len(secret_word):
    user_name = input("That was not 6 letters! Try again: ")

# Create variables for index and emoji as indicated in steps 
guess_indx: int = 0
emoji: str = ""

# Emoji is an empty string variable to allow for customization depending on the output i.e, green, white or yellow (Keep this in mind for multiple outputs in future)
while guess_indx < len(secret_word):
     if user_name[guess_indx] == secret_word[guess_indx]:
          emoji = (emoji + green_box)
     
     else: 
          place = False
          alt_indx: int = 0 
# This is a while loop within another while loop: (Need to understand this better)
          while place == False and alt_indx < len(secret_word):
# Now we are comparing the guess index of the "input" from the user (secret word), with the alternate index of the actual word 
               if secret_word[alt_indx] == user_name[guess_indx]:
                    place = True
               alt_indx = alt_indx + 1

          if place == True:
               emoji = emoji + yellow_box
          else: 
               emoji = (emoji) + white_box
     guess_indx = guess_indx + 1
print(emoji)

# Successful output
if user_name == secret_word:
     print("Woo! you got it!")

else:
     print("Not quite. Play again soon!")
