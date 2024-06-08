# it is the Hangman game. 1 - way

import random
from hangman_art import stages, logo
from hangman_words import word_list


word_list = word_list
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
letter_list = ["_"] * word_len
lives = 6
end_game = False
failed_letters = []

print(logo)
while not end_game:
    if len(failed_letters) > 0:
        print(f"Tried letters: {' '.join(failed_letters)}")
    guess = input("Guess a letter: ").lower()

    if not (guess in letter_list) and (guess in list(chosen_word)):

        for n in range(word_len):
            if chosen_word[n] == guess:
                letter_list[n] = guess

        print(f"{' '.join(letter_list)}")
        print(stages[lives])

        if not ("_" in letter_list):
            end_game = True
            print(f"Congrats. You found the word: {chosen_word}")

    elif guess in letter_list:
        print("You have already entered this letter!")
        print(f"{' '.join(letter_list)}")
        print(stages[lives])

    else:
        lives -= 1
        failed_letters.append(guess)

        print("The letter does not match the word! You lost one life!")
        print(f"{' '.join(letter_list)}")
        print(stages[lives])

        if lives <= 0:
            print(f"Uninformatively. The hidden word was: {chosen_word}")
            end_game = True
