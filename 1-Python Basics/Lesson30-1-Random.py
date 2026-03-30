import random
"""
number =random.randint(1,6) #random integer between 1 and 6
print(number)
"""
"""
low = 1
high = 100

number = random.randint(low,high)
print(number)
"""
"""
number = random.random() #random float between 0 and 1
print(number)
"""
"""
options = ["rock","Paper","Scissors"]
selection = random.choice(options)
print(selection)
"""
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)

stepper = random.randrange(0,20,2) #number between 0 and 20 stepped by 2
print(stepper)