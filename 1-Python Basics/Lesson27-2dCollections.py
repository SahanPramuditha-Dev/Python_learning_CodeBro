fruits =        ["apple","banana","cherry","dragon fruit"]
vegetables =    ["celery","carrots","potatoes"]
meats =         ["chicken","beef","pork"]

groceries = [fruits,vegetables,meats]

print(groceries)
print(groceries[0])
print(groceries[0][0])
print(groceries[1][1])
print(groceries[2][2])

print(len(groceries))
print(len(groceries[0]))

print("\n######################################\n")

groceries = [["apple","banana","cherry","dragon fruit"],["celery","carrots","potatoes"],["chicken","beef","pork"]]

print(groceries)

for collection in groceries:
    print(collection) #print collection by collection
    

print("\n######################################\n")

for collection in groceries:
    for item in collection:
        print(item,end=" ")
    print()

print("\n######################################\n")