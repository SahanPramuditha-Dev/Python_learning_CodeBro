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

# variable scope precedence order
# When you reference a variable in your code, Python looks for it in the following order:
# 1. Local scope: Python first looks for the variable in the local scope of the current function or block of code.
# 2. Enclosing scope: If the variable is not found in the local scope,
#    Python looks for it in the enclosing scope of any outer functions.
# 3. Global scope: If the variable is not found in the local or enclosing scopes
#    Python looks for it in the global scope of the module.
# 4. Built-in scope: If the variable is not found in the local, enclosing, or global scopes,
#    Python looks for it in the built-in scope of Python.

# LEGB - Local-> Enclosing-> Global-> Built-in














