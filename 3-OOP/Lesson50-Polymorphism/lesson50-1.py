# Polymorphism = "Many Forms"
# In OOP, polymorphism allows different objects to respond to the same method call
# in their own specific way.

# We import ABC (Abstract Base Class) and abstractmethod
# ABC allows us to create a blueprint class that cannot be instantiated directly.
from abc import ABC, abstractmethod


# ======================================
# Abstract Parent Class
# ======================================

class Shape(ABC):
    # This is an abstract method.
    # Any class that inherits Shape MUST implement this method./ who ever access shape class must create the area method definitely
    @abstractmethod
    def area(self):
        pass   # No implementation here (acts as a contract)


# ======================================
# Child Classes
# Each class implements its own version of area()
# ======================================

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Store radius value

    def area(self):
        # Area formula: πr²
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, width):
        self.width = width  # Store side length

    def area(self):
        # Area formula: side × side
        return self.width * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height  # Store base and height

    def area(self):
        # Area formula: ½ × base × height
        return 0.5 * self.base * self.height


# ======================================
# Polymorphism in Action
# ======================================

# We create objects of different classes
shapes = [Circle(4), Square(10), Triangle(3, 4)]

# Even though these are different classes,
# we can call the same method (.area()) on each object.
# This is polymorphism.
for s in shapes:
    print(f"Area is: {s.area()} cm²")