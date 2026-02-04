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


