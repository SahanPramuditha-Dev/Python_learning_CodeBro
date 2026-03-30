#get_ice_cream = add_chocolate(add_sprinkles(get_ice_cream))

# First decorator: add sprinkles
def add_sprinkles(func):
    def wrapper():
        print("Adding colorful sprinkles ✨")
        func()  # call the original function
        print("Sprinkles added 🍬")
    return wrapper

# Second decorator: add chocolate syrup
def add_chocolate(func):
    def wrapper():
        print("Adding chocolate syrup 🍫")
        func()  # Call the function from previous decorator
        print("Chocolate syrup added 🍫")
    return wrapper

# Decorated function with BOTH decorators
@add_chocolate   # outer decorator
@add_sprinkles   # inner decorator (applied first)
def get_ice_cream():
    print("Serving vanilla ice cream 🍦")

# Execute
get_ice_cream()
print("Your Ice Cream is Ready 🍨😋")