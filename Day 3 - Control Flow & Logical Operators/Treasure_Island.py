print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island! 🏝️")
print("Your mission is to find the hidden treasure. Choose wisely, adventurer! 💎")

# First choice at the crossroads
choice1 = input("You arrive at a crossroads. Do you want to go 'left' or 'right'? ⬅️➡️\n").lower()
if choice1 == "left":
    # Second choice at the lake
    choice2 = input("\nYou reach a tranquil lake 🌊. There's a boat 🚤 nearby, or you could swim 🏊 across. Do you want to 'wait' for the boat or 'swim' across? ").lower()
    if choice2 == "wait":
        print("\nYou patiently wait, and a boat arrives to take you across the lake. You land on an island with three mysterious houses: Red 🟥, Yellow 🟨, and Green 🟩.")
        # Third choice with doors
        choice3 = input("\nWhich door will you enter? Choose wisely: 'red' 🟥, 'yellow' 🟨, or 'green' 🟩? ").lower()
        if choice3 == "red":
            print("\nYou step through the Red door 🟥 and discover a chest filled with glittering gold and jewels! 🏆💰 Congratulations, you've found the treasure! 🎉")
        else:
            print("\nYou open the door... and it's empty. Game Over. 😞 Better luck next time.")
    elif choice2 == "swim":
        print("\nYou dive into the water 🌊, but suddenly, crocodiles 🐊 appear! You've been eaten. Game Over. 😱")
    else:
        print("\nInvalid choice! Please choose either 'wait' 🚤 or 'swim' 🏊.")
else:
    print("\nYou take the wrong path and are ambushed by a ferocious beast 🦁! Game Over. 😵")

