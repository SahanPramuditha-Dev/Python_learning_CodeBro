# List [] ordered , changeble , duplicates are okay
# Set {} unordered immutable add or remove okay no duplicates
# Tuple () ordered and unchangeble duplicates okay faster

fruits = ["Apple", "Banana", "Cherry","Dragon Fruit","Eggfruit","Fig","Grapes" ] 

"""
print(fruits)
print(fruits[0])
print(fruits[0:3])
print(fruits[::-1])
"""
"""
for fruit in fruits:
    print(fruit)#print fruits one by one in line by line
"""

"""

print(dir(fruits)) # tells you what actions you can perform on fruits
print(help(fruits)) #gives documentation about the object.
"""
#print(len(fruits)) #print length of fruis

#print("apple" in fruits) # if it is in the list it shows as true

fruits[0] = "Avacado"
print(fruits)


fruits.append("Zuccini") #add an item to the end of the list
print(fruits)

fruits.remove("Cherry") #remove an item from the list.it is case sensitiv
print(fruits)

fruits.insert(5,"Orange")
print(fruits)

fruits.sort() #when sorting they sort using uppercase lowercase also
print(fruits) #when sorting it changes the original list

#but if you need to keep the original list while sorting
# sorted_fruits = sorted(fruits) 

fruits.reverse()
print(fruits)


print(fruits.index("Eggfruit"))

fruits.clear() #clears the list
print(fruits)













