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


result = sqrt(16)
print(result)  # Output: 4.0

circumference = 2 * pi * 5
print(circumference)  # Output: 31.41592653589793

