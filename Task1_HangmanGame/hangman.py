import random
import hangman_stages

# List of predefined words
word_list = ["infoses", "codealpha", "google", "tcs", "microsoftg"]

# Number of incorrect guesses allowed
lives = 6

# Select a random word
chosen_word = random.choice(word_list)

# Initialize display with underscores for each letter
display = []
for i in range(len(chosen_word)):
    display += "_"

# Game loop control
game_over = False

# Track guessed letters to avoid duplicates
guessed_letters = set()

# Main game loop
while not game_over:
    print("\n" + hangman_stages.stages[6 - lives])  # Display the current hangman stage
    print("Word:", " ".join(display))  # Display the word with spaces for clarity
    print(f"Lives remaining: {lives}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")

    # Get user input
    guessed_letter = input("Guess a letter: ").lower()

    # Input validation
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("Please enter a single letter!")
        continue

    # Check for duplicate guesses
    if guessed_letter in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add the letter to guessed letters
    guessed_letters.add(guessed_letter)

    # Check if the letter is in the word
    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter
    else:
        lives -= 1
        print("Incorrect guess!")

    # Check win condition
    if "_" not in display:
        game_over = True
        print("\n" + hangman_stages.stages[6 - lives])
        print("Word:", " ".join(display))
        print("You win!!")

    # Check lose condition
    if lives == 0:
        game_over = True
        print("\n" + hangman_stages.stages[6 - lives])
        print("Word:", " ".join(display))
        print(f"You lose!! The word was '{chosen_word}'.")