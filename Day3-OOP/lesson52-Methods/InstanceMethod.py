# 1. Instance Methods (The "Resident")
# These methods are for things a specific house does. They use the self keyword because they need to know the specific details of that one house (like its address or color).

# Example: Painting the house. You can't just "paint"—you have to paint a specific house.

class House:
    def __init__(self, color):
        self.color = color  # Specific to this house

    # INSTANCE METHOD: Needs 'self' to know which house to paint
    def paint_house(self, new_color):
        self.color = new_color
        print(f"This specific house is now {self.color}")

my_house = House("Blue")
my_house.paint_house("Red") # Works on 'my_house' only