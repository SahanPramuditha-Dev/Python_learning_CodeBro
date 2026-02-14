# List - a concise way to create lists
# List comprehension is a powerful and concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for list comprehension is as follows:
# new_list = [expression for item in iterable if condition]
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

print("\n-----------------------------\n")