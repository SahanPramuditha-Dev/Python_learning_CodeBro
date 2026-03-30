for x in range(1, 11): #don not include ending numbers
    print(x) #numbers printed downwards one by one

print("\n#######################################################\n")

for y in reversed(range(1,11)):
    print(y)
print("Happy New Year !")

print("\n#######################################################\n")

for z in range(1,11,2): #to count two by two begining from 1
    print(z)

credit_card_number = "1234-5678-9012-3456"

for x in credit_card_number: #iterate through every number in the credit card
    print(x)

    print("\n#######################################################\n")

for x in range(1, 20):
    if x ==13:
        continue # continue will miss the 13th number and print the rest
    else:
        print(x)

print("\n#######################################################\n")

for x in range(1, 20):
    if x ==13:
        break # break will stop the loop from 13th on and stop the numbers till 12
    else:
        print(x)