"""
Decorator Concept (Ice Cream Analogy)
The ice cream = your original function
The sprinkles = extra behavior you add
A decorator = something that wraps the ice cream and enhances it without changing the original

"""

# ==============================
# DECORATOR DEFINITION
# ==============================

def add_sprinkles(func):
    """
    Decorator function
    - Takes another function as input (ice cream)
    - Adds extra behavior (sprinkles)
    """

    def wrapper(*args,**kwargs): # *To Accept Any Number of Arguments- without it we cant pass arguments
        # Extra behavior BEFORE original function
        print("Adding colorful sprinkles ✨")

        # Call the original function (ice cream)
        func(*args,**kwargs)

        # Extra behavior AFTER original function
        print("Sprinkles added successfully 🍬")

    return wrapper   # Return the wrapped function

def add_syrup(func): # *To Accept Any Number of Arguments- without it we cant pass arguments
    def wrapper(*args,**kwargs):
        print("Adding Chocolate Syrup")
        func(*args,**kwargs)
        print("Chocolate Syrup Added Successfully 🍫")
    return wrapper
    


# ==============================
# ORIGINAL FUNCTION (ICE CREAM)
# ==============================

@add_sprinkles
@add_syrup   # Applying decorator (adding sprinkles)
def get_ice_cream(flavor):
    print(f"Serving {flavor} ice cream 🍦")


# ==============================
# EXECUTION
# ==============================

get_ice_cream("Soya")