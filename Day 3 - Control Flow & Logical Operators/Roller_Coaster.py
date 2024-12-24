print("Welcome to the RollerCoaster!")
height = int(input("Enter height in cms: "))
bill = 0

if(height>=120):
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if(age<=12):
        bill+=5
        print("Please pay $5.")
    elif(age<=18):
        bill+=7
        print("Please pay $7.")
    elif(age>=45 and age<=55):
        print("Have a free ride!")
    else:
        bill+=12
        print("Please pay $12.")
    
    wants_photo = input("Do you want to have a photo taken? y for Yes or n for No.\n")
    if(wants_photo == "y"):
        bill+=3
    print(f"Total bill = {bill}")
else:
    print("Sorry, you cannot ride the rollercoaster!")