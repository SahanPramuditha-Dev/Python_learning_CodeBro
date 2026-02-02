# Creating a tuple named 'fruits'
# A tuple is an ordered, immutable collection of items
fruits = ("Apple", "Banana", "Cherry", "Cherry")

# Printing the entire tuple
print(fruits)  
# Output: ('Apple', 'Banana', 'Cherry', 'Cherry')


# 🔹 Using count() method
# count() returns how many times a value appears in the tuple
cherry_count = fruits.count("Cherry")
print("Cherry appears", cherry_count, "times")
# Output: Cherry appears 2 times


# 🔹 Using index() method
# index() returns the position of the FIRST occurrence of a value
banana_index = fruits.index("Banana")
print("Banana is at index:", banana_index)
# Output: Banana is at index: 1


# 🔹 Accessing tuple elements using index numbers
print("First fruit:", fruits[0])   # Apple
print("Last fruit:", fruits[-1])   # Cherry


# 🔹 Looping through a tuple
print("All fruits in the tuple:")
for fruit in fruits:
    print(fruit)


# ❗ Trying to change a tuple will cause an error because tuples are immutable
# fruits[0] = "Mango"   # This would raise: TypeError
