"""
DUCK TYPING IN PYTHON:
A programming philosophy that prioritizes an object's behavior over its 
actual class or type. 

The 'Duck Test' Principle:
'If it looks like a duck, swims like a duck, and quacks like a duck, 
then it probably is a duck.'
""" 

import os
from playsound3 import playsound # Ensure you ran: pip install playsound3

# --- HELPER FUNCTIONS ---

def get_audio_path(filename):
    """
    Constructs an absolute path to an audio file located in the script's directory.
    This prevents 'File Not Found' errors when running the script from different locations.
    """
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)

# --- CLASSES ---

class Animal:
    """Base class for all living creatures."""
    alive = True

class Dog(Animal):
    def speak(self):
        """Prints a bark and plays the corresponding audio file."""
        print("Woof Woof !")
        playsound(get_audio_path("Dog.mp3"))
        # print(get_audio_path("Dog.mp3")) #to visulaize the path

class Cat(Animal):
    def speak(self):
        """Prints a meow and plays the corresponding audio file."""
        print("Meow !")
        playsound(get_audio_path("Cat.mp3"))

class Car:
    """
    A non-animal class that still implements a 'speak' method.
    This is the core of Duck Typing: the loop below treats Car like an Animal
    simply because it possesses the 'speak' behavior.
    """
    def speak(self):
        print("I am Knight Industries 2000. You can call me KITT")
        playsound(get_audio_path("KITT_Intro.mp3"))
        playsound(get_audio_path("KITT.mp3"))

# --- MAIN EXECUTION ---

# Create a heterogeneous list (different types: Animals and Cars)
animals = [Dog(), Cat(), Car()]

# POLYMORPHISM IN ACTION: 
# We don't check 'isinstance(animal, Animal)'. 
# We just call the method and let Python's dynamic nature handle it.
for animal in animals:
    animal.speak()