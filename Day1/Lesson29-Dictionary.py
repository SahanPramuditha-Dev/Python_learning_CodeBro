#dictonary =  a collection of {key:value} pairs
#             ordered and changeable. No duplicates 



capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(capitals.get("USA"))
"""
if capitals.get("Russia"):
    print(capitals.get("Russia"))
else:
    print("Not Found")
"""

# print(capitals.get("japan","Not Found")) #to shorten if not found

"""
capitals.update({"Germany":"Berlin"})
print(capitals.get("Germany"))

"""

"""
capitals.pop("China")
print(capitals)
"""
"""
capitals.popitem() #removes the last item
print(capitals)
"""
"""
capitals.clear() #clears the dictionary
print(capitals)
"""
"""
keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)
"""

items = capitals.items()
print(items)



print("\n-----------------------------\n")


for key,value in capitals.items():
    print(f"{key} : {value}")

print("\n-----------------------------\n")


people = {
    "p001": {"name": "Sahan", "age": 21},
    "p002": {"name": "Kamal", "age": 30},
    "p003": {"name": "Nimal", "age": 25}
}

print(people["p002"]["age"])  # Output: 30

print("\n-----------------------------\n")

for person_id, details in people.items():
    print(f"{person_id} => Name: {details['name']}, Age: {details['age']}")

print("\n-----------------------------\n")


people = [
    {"name": "Sahan", "age": 21},
    {"name": "Kamal", "age": 30},
    {"name": "Nimal", "age": 25}
]

for person in people:
    print(person["name"], person["age"])

print("\n-----------------------------\n")

