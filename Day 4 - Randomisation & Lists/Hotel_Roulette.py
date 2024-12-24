import random

friends = ["Alex","Candice","Dan","Siva","Manoj"]

# Method 1
print(random.choice(friends))

# Method 2
n = len(friends)
random_index = random.randint(0,n-1)
print(friends[random_index])