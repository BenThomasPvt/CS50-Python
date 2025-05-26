import random
import sys


def correct(n):
    while True:
        try:
            number = int(input(n))
            if number > 0:
                return number
        except ValueError:
            pass


def main():
    level = correct("Level: ")
    n = random.randint(1, level)
    while True:
        guess = correct("Guess: ")

        if guess == n:
            print("Just right!")
            sys.exit()
        elif guess > n:
            print("Too large!")
        else:
            print("Too small!")


main()
