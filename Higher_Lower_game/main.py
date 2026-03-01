import random
from game_data import data
import art

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(account_a,account_b,user_guess):
    """Compare the user_guess."""
    if account_a > account_b:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def game():
    score =0

    print(art.logo)

    game_over = False

    account_b = random.choice(data)
    # repeat until user choose wrong
    while not game_over:

        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        print("\n" * 20)
        print(art.logo)
        while user_guess not in ['a', 'b']:
            user_guess = input("Please type 'A' or 'B': ").lower()

        is_correct= check_answer(account_a['follower_count'],account_b['follower_count'],user_guess)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
game()