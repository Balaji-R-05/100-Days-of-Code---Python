print("Welcome to Pizza Shop!")

# Getting pizza size
size = input("What pizza size do you want? S (Small), M (Medium), L (Large): ").upper()

# Initializing the bill
bill = 0

# Handling size choice
if size == "S":
    bill += 15
elif size == "M":
    bill += 24
elif size == "L":
    bill += 35
else:
    print("Invalid size entered! Please enter S, M, or L.")

# Getting toppings choice
topping_choice = input("What topping would you like? P (Pepperoni), M (Mushroom): ").upper()

# Adding topping cost
if topping_choice == "P":
    bill += 4
elif topping_choice == "M":
    bill += 5
else:
    print("Invalid topping choice! Please enter P or M.")

# Extra cheese option
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Adding cheese cost
if extra_cheese == "Y":
    bill += 2
elif extra_cheese != "N":
    print("Invalid choice for extra cheese! Please enter Y or N.")

# Display final bill
print(f"Your final bill is: ${bill}")