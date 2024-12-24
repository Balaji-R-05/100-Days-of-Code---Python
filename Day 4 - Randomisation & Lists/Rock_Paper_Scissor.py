import random

# Representing choices
choices = ["✊ Rock", "📄 Paper", "✂️ Scissors"]

# User input
user_choice = int(input("What is your choice? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Validating user choice
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    # Computer choice
    computer_choice = random.randint(0, 2)

    # Display choices
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")
