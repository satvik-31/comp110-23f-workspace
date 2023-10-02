"""Creating Wordle!"""

__author__: str = "730517765"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_no: int = 1
    attempt: bool = False
    secret: str = "codes"
    while turn_no <= 6 and attempt is not True:
        print(f"=== Turn {turn_no}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn_no}/6 turns! ")
            attempt = True
        turn_no = turn_no + 1
    if attempt is False:
        print("X/6 - Sorry, try again tomorrow")


def contains_char(any_length: str, single_char: str )-> bool:
    """To find out if the letter belongs in the word."""
    assert len(single_char) == 1
    validity: bool = False
    char_idx: int = 0
    while validity is False and char_idx < len(any_length):
        if single_char == any_length[char_idx]:
            validity = True
        else: 
            char_idx = char_idx + 1
    return validity


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def emojified(guess: str, secret:str) -> str: 
    """To find out the placement of the correct letters."""
    assert len(guess) == len(secret)
    emoji: str = ""
    guess_idx: int = 0

    while guess_idx < len(secret):
        if guess[guess_idx] == secret[guess_idx]:
            emoji = emoji + green_box
        
        else:
            if contains_char(secret, guess[guess_idx]):
                emoji = emoji + yellow_box

            else:
                emoji = emoji + white_box
        guess_idx += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess until they provide guess of expected length."""
    first_try: str = input(f"Enter a {expected_length} character word: ")
    while len(first_try) != expected_length:
        first_try = input(f"That wasn't {expected_length} characters! Try Again: ")
    return first_try


if __name__ == "__main__":
    main()            
