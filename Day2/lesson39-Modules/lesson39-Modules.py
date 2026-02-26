# mdoule - modules are files that contain Python code. They can define functions, classes, and variables. They can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes it more maintainable and reusable.
# To use a module, you need to import it into your Python script. You can import a module using the `import` statement, followed by the name of the module. For example, if you have a module named `math`, you can import it like this:

import math
# Once you have imported a module, you can access its functions, classes, and variables using the dot notation. For example, to use the `sqrt` function from the `math` module, you can do this:
result = math.sqrt(16)
print(result)  # Output: 4.0

# you can have alises for modules to make them easier to use. For example, you can import the `math` module with an alias like this:
import math as m
result = m.sqrt(16)
print(result)  # Output: 4.0

#you can also import specific functions, classes, or variables from a module using the `from` keyword. For example, to import only the `sqrt` function from the `math` module, you can do this:
from math import sqrt
from math import pi
from math import sqrt as s
from math import e

result = sqrt(25)
print(result)  # Output: 5.0

result = s(16)
print(result)  # Output: 4.0

circumference = 2 * pi * 5
print(circumference)  # Output: 31.41592653589793


result = e ** 2
print(result)  # Output: 7.38905609893065

# or you can import the module and then import specific functions from it:
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)       # Output: 3.141592653589793


a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)  # Output: 1 2 3 4

"""
in above a = 1, b = 2, c = 3, d = 4 is an example of unpacking, where we assign values to multiple variables in a single line. This is a convenient way to initialize multiple variables at once, and it can make your code more concise and readable.

number of variables on the left side of the assignment operator (=) must match the number of values on the right side. If they do not match, Python will raise a ValueError. For example, if you try to unpack three values into two variables like this:

a, b = 1, 2, 3 # This will raise a ValueError: too many values to unpack (expected 2)

"""







