# List - a concise way to create lists
# List comprehension is a powerful and concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for list comprehension is as follows:
# new_list = [expression for item in iterable if condition]

"""
list comprehension always follows this pattern:
[ WHAT_TO_DO  for item in collection  if CONDITION ]

- WHAT_TO_DO: This is the expression that defines what you want to do with each item in the collection. It can be any valid Python expression that operates on the item.
- for item in collection: This is the loop that iterates over each item in the collection
- if CONDITION: This is an optional part that allows you to filter items based on a condition. Only items that satisfy the condition will be included in the new list.

# in English
#   “For each item in the collection, if the condition is true, do this thing and store the result.”

Correct Example (Odd numbers)

odd = [num for num in numbers if num % 2 != 0]
print(odd)

How Python reads this:
odd = []

for num in numbers:                 # Loop
    if num % 2 != 0:                # Condition (FILTER)
        odd.append(num)             # WHAT TO DO

# Generalized Template for List Comprehension

result = [ X  for item in iterable  if Y ]


"""




# Here are some examples to illustrate how list comprehension works:

doubles = []
for x in range (1,11):
    doubles.append(x*2)
print(doubles)

# we can achieve the same result using list comprehension in a more concise way:
doubles = [x*2 for x in range(1,11)]
print(doubles)

print("\n-----------------------------\n")

triples = { x*3 for x in range(1,11) }
print(triples)

print("\n-----------------------------\n")

squares = { x*x for x in range(1,11) }
print(squares)

print("\n-----------------------------\n")


fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)

print("\n-----------------------------\n")

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive = [num for num in numbers if num > 0]
print(positive)

negative = [num for num in numbers if num < 0]
print(negative)

even = [num for num in numbers if num % 2 == 0]
print(even)

odd = [num for num in numbers if num % 2 != 0]
print(odd)




print("\n-----------------------------\n")







