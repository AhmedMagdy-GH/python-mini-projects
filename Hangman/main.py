import random
import hangman_words
import hangman_arts

print(hangman_arts.logo)
chosen_word= random.choice(hangman_words.word_list)

game_over=False

correct_letters=[]

display=""

lives=6

place_holder=""

print(chosen_word)

while not game_over:

    for letter in chosen_word:
        place_holder+="-"
    print("Word to guess: "+place_holder)

    print(f"********************************{lives}/6 LIVES LEFT********************************")

    display = ""
    guess=input("choose a letter:").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print("Word to guess: " + display)

    print(hangman_arts.stages[lives])

    if display == chosen_word:
        print("********************************YOU WON********************************")
        game_over=True

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word, you lose a life.")
        if lives == 0:
            print(hangman_arts.stages[lives])
            print(f"********************************IT WAS {chosen_word}! YOU LOSE********************************")
            game_over = True
