# Super Parent class . all classese inherit properties and methods from here

class Animal:
    """Provides basic shared behaviors for all animals."""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")


# SINGLE INHERITANCE

# Prey inherits from Animal (One parent)
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is running away!")

# Predator inherits from Animal (One parent)
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

# Rabbit inherits from Prey (A single line: Rabbit -> Prey -> Animal)
class Rabbit(Prey):
    pass

# Hawk inherits from Predator (A single line: Hawk -> Predator -> Animal)
class Hawk(Predator):
    pass


# MULTIPLE INHERITANCE

# Fish inherits from BOTH Prey and Predator classes.
# It gains 'flee' from Prey and 'hunt' from Predator.
class Fish(Prey, Predator):
    pass


# Object Creation

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Finley")

# --- Single Inheritance ---
print(f"--- {rabbit.name} ---")
rabbit.flee()   # Comes from Prey class
rabbit.eat()    # Comes from Animal class

print(f"\n--- {hawk.name} ---")
hawk.hunt()     # Comes from Predator class
hawk.sleep()    # Comes from Animal class

# --- Multiple Inheritance---
print(f"\n--- {fish.name} ---")
fish.flee()     # Gains this because it is a Prey
fish.hunt()     # Gains this because it is a Predator
fish.eat()      # Gains this because both parents are Animals