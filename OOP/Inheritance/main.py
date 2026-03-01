# --- THE PARENT (SUPER) CLASS ---
# This class defines the general attributes and behaviors that all animals share.
class Animal:
    def __init__(self, name, food, toy):
        # 'self' refers to the specific instance of the animal being created.
        self.name = name
        self.food = food
        self.toy = toy
        self.is_alive = True  # A default attribute shared by all animals

    def eat(self):
        # Method to simulate eating; uses the specific food assigned to the instance.
        print(f"{self.name} eats {self.food}.")

    def play(self):
        # Method to simulate playing; uses the specific toy assigned to the instance.
        print(f"{self.name} plays with {self.toy}")

# --- THE CHILD (SUB) CLASSES ---
# By putting 'Animal' in parentheses, these classes "inherit" everything from Animal.

class Dog(Animal):
    # 'pass' is a placeholder. It means this class has no unique code of its own yet,
    # but it still gets all the features of the Animal class.
    pass

class Cat(Animal):
    pass

class Dolphin(Animal):
    pass

# --- INSTANTIATION (Creating Objects) ---
# We provide the specific 'name', 'food', and 'toy' for each animal.
dog = Dog("Scooby Doo", "Meat", "Disc")
cat = Cat("Garfield", "Lasangya", "Pooky Bear")
dolphin = Dolphin("Sam", "Salman", "Ball")

# --- EXECUTION ---

# Accessing attributes and methods from the Dog instance
print(f"Dogs name is {dog.name}.")
dog.eat()
dog.play()

print("\n------------------------------------\n")

# Even though Cat is empty (pass), it can use 'is_alive' and 'eat()' from Animal.
print(f"Cats name is {cat.name}.")
print(f"Is he alive: {cat.is_alive}")
cat.eat()
cat.play()

print("\n------------------------------------\n")

# Accessing the Dolphin instance
print(f"Dolphin's name is {dolphin.name}.")
print(f"Is he alive: {dolphin.is_alive}")
dolphin.eat()
dolphin.play()