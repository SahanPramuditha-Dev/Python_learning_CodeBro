def shipping_address(*args, **kwargs):
    print("Shipping Address:")
    for arg in args:
        print(arg,end=" ")  # Output: John Doe 123 Main St Anytown USA, the values of the non-keyword arguments are printed in a single line, separated by spaces.
    print()  # Print a newline after the non-keyword arguments are printed.
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}"
              )

shipping_address("John Doe", "123 Main St", "Anytown", "USA",
                 zip_code="12345", phone="555-1234")

##only work when we set args first and then kwargs, because if we set kwargs first and then args, it will raise a SyntaxError because Python expects positional arguments (args) to come before keyword arguments (kwargs) in a function definition. Therefore, we need to define the function with *args first and then **kwargs to allow for both types of arguments to be passed correctly.

"""
def shipping_address(**kwargs, *args):
    print("Shipping Address:")

shipping_address("John Doe", "123 Main St", "Anytown", "USA",
                 zip_code="12345", phone="555-1234")

#this will raise a SyntaxError because Python expects positional arguments (args) to come before keyword arguments (kwargs) in a function definition. Therefore, we need to define the function with *args first and then **kwargs to allow for both types of arguments to be passed correctly.





"""

print("\n\n-----------------------------\n")


def shipping_address(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"House Number:{kwargs['house_number']}")
    print(f"Zip Code: {kwargs['zip_code']}")
    print(f"Phone: {kwargs['phone']}")

shipping_address("John Doe", "123 Main St", "Anytown", "USA",
                 zip_code="12345", phone="555-1234", house_number="221/B")






