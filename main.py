import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear


print(logo)
print("Welcome to HANGMAN!")

# Games ends if number of lives reach 0.
lives = 6

# User have to guess the random word.
chosen_word = list(random.choice(word_list))
print(f"You have to guess a {len(chosen_word)} letter word.")

# For visual purposes.
print("")

# list for displaying the guess letter
display = []
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

# For visual purposes.
print("")

# Game will run as long as user have not guessed the word or user
# still have lives left. Game will end as soon as whichever of these
# two conditions comes first.
while chosen_word != display and lives > 0:

    guess = input("Please guess a letter: ").lower()

    # Clearing the console after each input (only works on replit)
    clear()

    if guess in display:
        print(f'You have already entered "{guess}".')
    else:
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed '{guess}', which is not in the word. "
                  f"You lose a life.")

        # Replaces the _ with the guessed letter if it's in the word.
        position = 0
        for letter in chosen_word:
            position += 1
            if letter == guess:
                display[position - 1] = letter

        print(f"{' '.join(display)}")
        print(stages[lives])

if chosen_word == display:
    print("You win.")
else:
    print("You lose.")
    print(f'The word was "{"".join(chosen_word)}".')
