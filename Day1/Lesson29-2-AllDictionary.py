# Creating a dictionary
capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# Accessing values
print("Russia's capital:", capitals["Russia"])  # Direct access
print("Germany's capital:", capitals.get("Germany"))  # Safe access (returns None)

# Dictionary views
print("Keys:", capitals.keys())
print("Values:", capitals.values())
print("Items:", capitals.items())

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in capitals.items():
    print(key, "->", value)

# Updating dictionary
capitals.update({"Germany": "Berlin"})  # Add new
capitals.update({"USA": "Las Vegas"})   # Modify existing
print("\nAfter update:", capitals)

# Removing elements
removed = capitals.pop("China")  # Remove specific key
print("\nRemoved China which had capital:", removed)

last_item = capitals.popitem()  # Remove last inserted pair
print("Removed last inserted pair:", last_item)

# setdefault() - Adds only if key does not exist
capitals.setdefault("France", "Paris")   # Added
capitals.setdefault("USA", "New York")   # Won’t change
print("\nAfter setdefault:", capitals)

# copy() - Shallow copy
copy_capitals = capitals.copy()
print("\nCopied dictionary:", copy_capitals)

# fromkeys() - Create dictionary with default values
countries = ["Japan", "Korea", "Thailand"]
new_dict = dict.fromkeys(countries, "Unknown")
print("\nDictionary from keys:", new_dict)

# Checking membership
print("\nIs 'India' a key?", "India" in capitals)
print("Is 'Paris' a value?", "Paris" in capitals.values())

# Length of dictionary
print("\nNumber of entries:", len(capitals))

# Delete using del
del capitals["USA"]
print("\nAfter deleting USA:", capitals)

# Dictionary comprehension
squares = {x: x * x for x in range(5)}
print("\nDictionary comprehension (squares):", squares)

# Nested dictionary
students = {
    "Sahan": {"age": 21, "grade": "A"},
    "Nimal": {"age": 22, "grade": "B"}
}
print("\nNested dictionary example:")
print("Sahan's grade:", students["Sahan"]["grade"])

# clear() - Remove everything
capitals.clear()
print("\nAfter clear():", capitals)
