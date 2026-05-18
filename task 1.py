# ==========================================
# HANGMAN GAME
# ==========================================

import random

# List of predefined words
words = ["python", "apple", "laptop", "engineer", "college"]

# Randomly choose one word
secret_word = random.choice(words)

# Empty list to store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

print("===== WELCOME TO HANGMAN =====")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with underscores
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the whole word
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter to list
    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
