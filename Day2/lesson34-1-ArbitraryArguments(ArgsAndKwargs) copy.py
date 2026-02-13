# arbutrary Aarguments means that we can pass a variable number of arguments to a function. This is useful when we don't know in advance how many arguments will be passed to the function.




# *args    - allows you to pass mutiple non-key arguments
# **kwargs - allows you to pass mutiple key arguments


def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
# print(add(12, 3, 4, 5))  #if we try to pass more than 2 arguments, it will raise a TypeError because the add function is defined to take only 2 parameters (a and b), but we are trying to pass 4 arguments

def add(*args):
    print(type(args))  # Output: <class 'tuple'>, *args collects all the non-keyword arguments into a tuple named args.


add() # Output: () - an empty tuple, because we didn't pass any arguments to the add function.

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(2, 3))  # Output: 5
print(add(12, 3, 4, 5))  # Output: 24

def sub(*nums):
    total = 0
    for num in nums:
        total -= num
    return total

print(sub(2, 3))  # Output: -5
print(sub(12, 3, 4, 5))  # Output: -24













