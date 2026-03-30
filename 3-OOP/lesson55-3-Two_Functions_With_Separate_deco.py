# ==============================
# file2.py
# Two functions decorated separately
# ==============================

# Decorator: add sprinkles
def add_sprinkles(func):
    def wrapper():
        print("Adding colorful sprinkles ✨")
        func()
        print("Sprinkles added 🍬")
    return wrapper

# Decorator: add chocolate syrup
def add_chocolate(func):
    def wrapper():
        print("Adding chocolate syrup 🍫")
        func()
        print("Chocolate syrup added 🍫")
    return wrapper

# First function decorated with sprinkles
@add_sprinkles
def vanilla_ice_cream():
    print("Serving vanilla ice cream 🍦")

# Second function decorated with chocolate syrup
@add_chocolate
def chocolate_ice_cream():
    print("Serving chocolate ice cream 🍫")

# Execute both
vanilla_ice_cream()
print("------------------------")
chocolate_ice_cream()