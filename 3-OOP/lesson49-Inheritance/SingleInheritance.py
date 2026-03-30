# --- THE PARENT (SUPER) CLASS ---
# A blueprint for the general "Animal". Any common trait goes here.
# This class defines the general attributes and behaviors that all animals share.
#helps with resuability and extensibility
# class Child(Parent)


class Animal:
    def __init__(self, name, food, toy):
        # 'self' refers to the specific instance of the animal being created.
        # Initializing instance attributes
        self.name = name
        self.food = food
        self.toy = toy
        self.is_alive = True  # A default attribute shared by all animals

    def eat(self):
        # Shared method: All animals eat
        # Method to simulate eating; uses the specific food assigned to the instance.
        print(f"{self.name} eats {self.food}.")

    def play(self):
        # Shared method: All animals play
        # Method to simulate playing; uses the specific toy assigned to the instance.
        print(f"{self.name} plays with {self.toy}")

# --- THE CHILD (SUB) CLASSES ---
# By putting 'Animal' in parentheses, these classes "inherit" everything from Animal.
# These classes inherit (receive) all attributes and methods from Animal.

class Dog(Animal):
    def bark(self):
        # Unique Method: Only Dog objects can access this
        print(f"{self.name} Barks.")

class Cat(Animal):
    def meow(self):
        # Unique Method: Only Cat objects can access this
        print(f"{self.name} Meows.")

class Dolphin(Animal):
    # 'pass' is a placeholder. It means this class has no unique code of its own yet,
    # but it still gets all the features of the Animal class.
    # Using 'pass' means this class is an exact copy of Animal with no extras
    pass

# --- INSTANTIATION (Creating Objects) ---
# We provide the specific 'name', 'food', and 'toy' for each animal.
# Creating specific objects (instances) of the classes
dog = Dog("Scooby Doo", "Meat", "Disc")
cat = Cat("Garfield", "Lasangya", "Pooky Bear")
dolphin = Dolphin("Sam", "Salman", "Ball")

# --- EXECUTION ---

# Accessing attributes and methods from the Dog instance
print(f"Dogs name is {dog.name}.")
dog.eat()    # Inherited method
dog.play()   # Inherited method
dog.bark()   # Unique method

print("\n------------------------------------\n")

# Even though Cat is empty (pass), it can use 'is_alive' and 'eat()' from Animal.
print(f"Cats name is {cat.name}.")
print(f"Is he alive: {cat.is_alive}")
cat.eat()    # Inherited method
cat.play()   # Inherited method
cat.meow()   # Unique method (Fixed typo from 'mewo')

print("\n------------------------------------\n")

# Accessing the Dolphin instance
print(f"Dolphin's name is {dolphin.name}.")
print(f"Is he alive: {dolphin.is_alive}")
dolphin.eat()
dolphin.play()
# dolphin.bark() would cause an AttributeError because Dolphins can't bark!