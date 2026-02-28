from random import randint
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(user_guess, actual_answer, turns):
    """ Checks answer against guess, returns the number of turns remaining. """
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        level = EASY_LEVEL_TURNS
    else:
        level = HARD_LEVEL_TURNS
    return level


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()
    guess = -1

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let user guess a number
        guess = int(input("Make a guess:"))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game ()