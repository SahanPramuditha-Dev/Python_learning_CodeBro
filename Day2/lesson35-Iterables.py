# Iterables are objects that can be iterated over, meaning you can loop through them to access their elements one at a time. In Python, common iterables include lists, tuples, strings, dictionaries, and sets. Iterables are a fundamental concept in Python and are used in various contexts, such as loops, comprehensions, and functions that expect iterable inputs.

numbers = [1, 2, 3, 4, 5]  # This is a list, which is an iterable.

for num in numbers:
    print(num)  # Output: 1, 2, 3, 4, 5 vertically, each number is printed on a new line.

for num in reversed(numbers):
    print(num)  # Output: 5, 4, 3, 2, 1 vertically


print("\n-----------------------------\n") 

fruits = {"apple", "banana", "cherry"}  # This is a set, which is also an iterable.

for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry vertically


"""
for fruit in reversed(fruits):
    print(fruit)  # cant reverse a set because sets are unordered collections, meaning that the elements do not have a defined order. Therefore, you cannot reverse a set using the reversed() function or any other method that relies on the order of elements. If you need to reverse the elements of a set, you would first need to convert it to a list or another ordered collection, and then reverse that collection. However, keep in mind that the original set does not maintain any order, so the concept of reversing it does not apply directly to sets.



"""
print("\n-----------------------------\n")

my_dict = {"name": "John", "age": 30, "city": "New York"}  # This is a dictionary, which is also an iterable.

for key in my_dict:
    print(key)  # Output: name, age, city vertically


print("\n-----------------------------\n")


for value in my_dict.values():
    print(value)  # Output: John, 30, New York vertically

print("\n-----------------------------\n")

for key in my_dict.keys():
    print(key)  # Output: name, age, city vertically

print("\n-----------------------------\n")

"""
COMPARISON: Iterating over Dictionaries

| Feature     | for key in my_dict          | for key in my_dict.keys()   |
|-------------|-----------------------------|-----------------------------|
| Output      | Keys only                   | Keys only                   |
| Style       | Concise / Idiomatic (Best)  | Explicit                    |
| Speed       | Marginally faster           | Marginally slower           |
| Readability | High (Standard Python)      | High (Clear for beginners)  |


they asc as the same output but the first one is more concise and is considered more idiomatic in Python, while the second one is more explicit and may be clearer for beginners who are learning about dictionaries. In terms of performance, the difference is negligible for most use cases, but the first method can be slightly faster since it directly iterates over the dictionary keys without the overhead of calling the keys() method. Ultimately, both methods are valid and can be used based on personal preference or coding style guidelines.
"""

superheroes = {"Ironman": "Tony Stark", "Captain-America": "Steve Rogers", "Thor": "Thor Odinson", "Hulk": "Bruce Banner", "Black-Widow": "Natasha Romanoff", "Hawkeye": "Clint Barton", "Ant-Man": "Scott Lang", "Vision": "Vision", "Scarlet Witch": "Wanda Maximoff", "Doctor Strange": "Stephen Strange", "Black Panther": "T'Challa", "spiderman": "Peter Parker"}

for key,value in superheroes.items():
    print(f"{key} => {value}")

print("\n-----------------------------\n")


