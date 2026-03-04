# --- The Introspection Logic ---

#  To call methods without knowing their names beforehand, we use a process called Introspection.
#  This allows the program to "look in the mirror" and see what it is capable of doing.


# --- Our Setup ---
class Animal:
    def eat(self):
        print("Eating...")

class Rabbit(Animal):
    def flee(self):
        print("Running away!")

# Create the object (instance)
rabbit = Rabbit()

# 1. dir(rabbit) gives us a list of every name inside the object (as strings)
all_names = dir(rabbit) 

for name in all_names:
    # 2. Skip "Magic Methods" (Internal Python stuff like __init__ or __str__)
    # We only want our own custom methods.
    if not name.startswith("__"):
        
        # 3. getattr() converts the string name (like "eat") into the actual function
        attribute = getattr(rabbit, name)
        
        # 4. callable() checks if the attribute is a function we can run.
        # We don't want to try and "run" a variable like an age or a name.
        if callable(attribute):
            print(f"I found a method called: {name}")
            
            # 5. Add () to the end of the attribute to actually execute it
            attribute()