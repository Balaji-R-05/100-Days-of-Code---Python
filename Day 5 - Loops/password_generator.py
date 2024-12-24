import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+','_']

print("Welcome to Password Generator!")
print("-------------------------------")

nr_letters = int(input("Enter number of letters: "))
nr_numbers = int(input("Enter number of numbers: "))
nr_symbols = int(input("Enter number of symbols: "))

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_numbers):
    password.append(random.choice(numbers))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
print("-------------------------------")
print("Your password is: ", "".join(password))