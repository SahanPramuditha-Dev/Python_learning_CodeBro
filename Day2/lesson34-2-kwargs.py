# arbutrary Aarguments means that we can pass a variable number of arguments to a function. This is useful when we don't know in advance how many arguments will be passed to the function.

# *args    - allows you to pass mutiple non-key arguments
# **kwargs - allows you to pass mutiple key arguments

def type_of_kwargs(**kwargs):
    print(type(kwargs))
type_of_kwargs()  # Output: <class 'dict'>, **kwargs collects all the keyword arguments into a dictionary named kwargs.


print("-----------------------------\n")


def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")  # Output: 221/B Baker Street Marylebone London NW11 6XE, the values of the keyword arguments are printed in a single line, separated by spaces. However, the order of the values may vary each time you run the program due to the nature of dictionaries in Python.


def tonys_print_address(**kwargs):
    if not kwargs:
        print("No address provided.")
    else:
        for key, value in kwargs.items():
            print(f"{key.capitalize()}: {value}")




#if we pass the keyword arguments to the print_address function, it will print the values of the arguments in the order they were passed. However, since **kwargs collects the keyword arguments into a dictionary, the order of the values is not guaranteed, and it may vary each time you run the program. This is because dictionaries in Python do not maintain the order of their items until Python 3.7, where they started to preserve insertion order as an implementation detail. Therefore, when you run this code, you may see the address components printed in a different order each time.
print_address(house_number="221/B",
              street="Baker Street", 
              city="Marylebone", 
              country="London", 
              zip_code="NW11 6XE")

print("\n-----------------------------\n")

tonys_print_address(house_number="10880",
              street="Malibu Point", 
              city="Malibu",
              country="California", 
              zip_code="NW11 6XE")


