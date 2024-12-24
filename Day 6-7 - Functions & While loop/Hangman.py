import random

hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Word list
word_list = ["love", "python", "rust", "javascript", "java", "golang", "function", "method", "class"]
chosen_word = random.choice(word_list)

# Game setup
game_over = False
correct_letters = set()
no_of_turns = 6

print("Welcome to the Word Guessing Game!")
print("_ " * len(chosen_word))  # Initial display of underscores for the word

while not game_over and no_of_turns > 0:
    guess = input("Enter your guess (a single letter): ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    # Build the display string
    display = ""
    if guess in chosen_word:
        print(f"👏 Good job! '{guess}' is in the word.")
        correct_letters.add(guess)
    else:
        print(f" 😔 Sorry, '{guess}' is not in the word.")
        no_of_turns -= 1
        print(f"Turns remaining: {no_of_turns}")
        print(hangman_stages[6 - no_of_turns])

    for letter in chosen_word:
        display += letter if letter in correct_letters else "_"

    print(f"{display}")

    # Check for win condition
    if "_" not in display:
        print(f" 🎉 Congratulations! You guessed the word: {chosen_word}")
        game_over = True

# If out of turns
if no_of_turns == 0:
    print(f" ❌ Game Over! The word was: {chosen_word}")