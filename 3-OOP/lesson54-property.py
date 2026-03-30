"""
@property enables:
- Attribute-style access to methods
- Encapsulation with validation
- Clean and maintainable interface design
"""

class Rectangle:

    # ==============================
    # CONSTRUCTOR
    # ==============================
    def __init__(self, width, height):
        # Internal ("protected") variables
        # Convention: single underscore → not meant for direct external access
        self._width = width
        self._height = height


    # ==============================
    # GETTERS (READ ACCESS)
    # ==============================

    @property
    def width(self):
        """
        Getter for width
        - Accessed like: rectangle.width
        - Returns formatted value with unit
        """
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        """
        Getter for height
        - Same behavior as width
        """
        return f"{self._height:.1f} cm"


    # ==============================
    # SETTERS (WRITE ACCESS + VALIDATION)
    # ==============================

    @width.setter
    def width(self, new_width):
        """
        Setter for width
        - Validates input before assignment
        """
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):   # ✅ FIXED (was incorrectly named 'width')
        """
        Setter for height
        - Validates input before assignment
        """
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")


    # ==============================
    # OPTIONAL: COMPUTED PROPERTY
    # ==============================

    @property
    def area(self):
        """
        Derived property (read-only)
        - Demonstrates business logic encapsulation
        """
        return self._width * self._height
    
    # ==============================
    # OPTIONAL: DELETE PROPERTY
    # ==============================

    @height.deleter
    def height(self):
        del self._height
        print("Height has been Deleted")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been Deleted")
    


# ==============================
# TESTING THE CLASS
# ==============================

# Create object
rectangle = Rectangle(3, 4)

# Access properties (calls getters internally)
print(rectangle.width)      # 3.0 cm
print(rectangle.height)     # 4.0 cm

# Direct access (NOT recommended – breaks encapsulation)
print(rectangle._width)
print(rectangle._height)

# Update values using setters
rectangle.width = 5
rectangle.height = 6

print(rectangle.width)      # 5.0 cm
print(rectangle.height)     # 6.0 cm

# Computed property
print("Area:", rectangle.area)

# Delete the Properties
del rectangle.width
del rectangle.height


