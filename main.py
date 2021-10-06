"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.

def main():
    print(
        f'''
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
''')

    while True:
        secret_number = random_secret_number()
        print(f"secret_number: {secret_number}")
        print("I have thought up a number.")
        print(f" You have {MAX_GUESSES} guesses to get is.")
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input("> ")
                clues = get_clues(guess, secret_number)
                print(clues)
                num_guesses += 1
            if guess == secret_number:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out guesses.")
                print(f"The answer was {secret_number}")
        print("Do you want to play again ? (yes or no)")
        play_again = input("> ").lower().startswith("y")
        if not play_again:
            print("#"*40)
            break
        print("Thanks for playing!")
        print("#" * 40)
        print()

def random_secret_number():
    random_number = random.choices(range(10), k=NUM_DIGITS)
    return ''.join(map(str, random_number))

def get_clues(guess, secret_number):
    if guess == secret_number:
        return "You got it!"

    clues = []
    for index in range(len(guess)):
        if guess[index] == secret_number[index]:
            # A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess[index] in secret_number:
            # A correct digit is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == '__main__':
    main()