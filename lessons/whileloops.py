"""Explroing loops by finding low value in string"""

cards: str = "5235"

Card_indx: int = 0
low_card: int = int(cards[0])
#Look at each number in the string 
while Card_indx < 4:
    # check if current card is less thann low card
    current_card: int = int(cards[Card_indx])
    if (current_card < low_card):
        #Update the low card to be the value of the current card
        low_card = current_card
    Card_indx = Card_indx + 1
print(low_card)