# return - statement used to end a function
#          and send a result back to the caller

"""
def add(a,b):
    Z = a + b
    return Z

def sub(a,b):
    Z = a - b
    return Z

def mul(a,b):
    Z = a * b
    return Z

def div(a,b):
    Z = a / b
    return Z

print(add(2,3))
print(sub(2,3))
print(mul(2,3))
print(div(2,3))


"""

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

name = create_name("sahan","perera")
print(name)