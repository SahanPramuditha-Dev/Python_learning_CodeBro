# Scope Resolution in Python
# variable scope is where a variable is accessible in your code.
#  In Python, there are four types of variable scopes:
#  local, enclosing, global, and built-in.
#  The scope of a variable determines where it can be accessed and modified in your code.





# local scope example
def my_function():
    x = 10  # x is a local variable, it is only accessible within this function
    print(x)

my_function()  # Output: 10

# trying to access x outside of the function will raise a NameError
# print(x)  # This will raise a NameError: name 'x' is not defined

#Enclosing scope example
def outer_function():
    y = 20
    def inner_function():
        print(y)
    inner_function()

outer_function()  # Output: 20

# trying to access y outside of the functions will raise a NameError

#global scope example
z = 30  # z is a global variable, it is accessible throughout the entire program
def my_function():
    print(z)
my_function()  # Output: 30
print(z)  # Output: 30

# built-in scope example
# built-in functions and variables are always available in Python, and they are part of the built

from math import e

def function():
    print(e)  # e is a built-in variable, it is accessible within this function

e= 3

print(e)  # Output: 3
function()  # Output: 2.718281828459045

















