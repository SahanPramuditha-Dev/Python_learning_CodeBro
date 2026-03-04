class Car:
    # Class Variable (Shared by all cars)
    base_price = 20000 

    def __init__(self, model, color):
        # Instance Variables (Unique to each car)
        self.model = model
        self.color = color

    # 1. INSTANCE METHOD
    # Use: When you need to access specific data about ONE car (self)
    def describe_car(self):
        return f"This is a {self.color} {self.model}."

    # 2. STATIC METHOD
    # Use: A "utility" tool. It doesn't need to know about a car's color or model.
    # It just performs a logic check or calculation.
    @staticmethod
    def is_vintage(year):
        return year < 1995  # Returns True or False regardless of the specific car object

    # 3. CLASS METHOD
    # Use: When you want to see or change something that affects EVERY car (cls)
    @classmethod
    def set_base_price(cls, amount):
        cls.base_price = amount
        print(f"Base price for all cars updated to: ${cls.base_price}")

# --- HOW TO USE THEM ---

# Create an instance (object)
my_car = Car("Tesla", "Red")

# 1. Calling the Instance Method
# It knows it is a 'Red Tesla' because of 'self'
print(my_car.describe_car()) 

# 2. Calling the Static Method
# We call it via the CLASS name. We don't even need 'my_car' to exist to run this.
print(f"Is a 1980 car vintage? {Car.is_vintage(1980)}") 

# 3. Calling the Class Method
# This changes 'base_price' for the entire Blueprint (Class)
Car.set_base_price(25000)