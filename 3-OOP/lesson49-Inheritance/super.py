# is a built-in function that allows a child class to call methods from its parent class.
# It is the standard way to ensure that the "parent's logic" is executed before or after the child's specific logic.


import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def get_area(self):
        # Accessing self.radius to calculate area: πr²
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def get_area(self):
        # Accessing self.width to calculate area: w²
        return self.width ** 2

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def get_area(self):
        # Accessing multiple attributes: (w * h) / 2
        return (self.width * self.height) / 2

# --- Instances ---
circle = Circle("Red", True, 5)
square = Square("Blue", False, 10)

# Using Keyword Arguments (Makes the code very readable!)
triangle = Triangle(color="Green", is_filled=False, width=15, height=10)

# --- Enhanced Accessing ---

print("--- Circle Access ---")
print(f"Color: {circle.color}")           # Accessing parent attribute
print(f"Radius: {circle.radius}")         # Accessing child attribute
print(f"Area: {circle.get_area():.2f}")   # Accessing via a method calculation

print("\n--- Square Access ---")
# Using a conditional access to check fill status
status = "Filled" if square.is_filled else "Empty"
print(f"The {square.color} square is currently {status}.")
print(f"Area: {square.get_area()}")

print("\n--- Triangle Access ---")
# Accessing multiple dimensions at once
print(f"Dimensions: {triangle.width}w x {triangle.height}h")
print(f"Total Area: {triangle.get_area()}")

# --- Batch Accessing (Realistic Scenario) ---
print("\n--- Processing All Shapes ---")
shapes = [circle, square, triangle] #objects

for s in shapes:
    # Using type() to access the class name dynamically
    print(f"Shape: {type(s).__name__} | Color: {s.color} | Area: {s.get_area():.1f}")







