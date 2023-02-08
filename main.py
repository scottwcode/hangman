# This python program "plays hangman" by randomly selecting a word
# from a list of words from hangman_words.py and prompts the user
# to pick letters they think are part of the word. They have 6 attempts
# at missing letters, before they lose. If they guess all the letters in
# the random word before missing 6 attempts, they win. Guessing the same
# letter multiple times has no consequence.

from hangman_art import logo
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_game = False
attempts = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# Testing - show the random word
# print(f'The solution is {chosen_word}.')

# Create a set with a blank "_" for each letter of the random word
display = []
for _ in range(word_length):
    display += "_"

while not end_game:
    guess = input("Please guess a letter: ").lower()

# If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}. Try again")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        # Check if user guessed correctly and add the letter(s) to the display
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(
            f"You guessed {guess}, that's not in the word. You lose an attempt.")

        attempts -= 1
        if attempts == 0:
            end_game = True
            print("Out of attempts. You lose :-(")
            print(f"The word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_game = True
        print("You've correctly guessed the word! You win!!!")

    # Import the stages from hangman_art.py
    from hangman_art import stages
    print(stages[attempts])
