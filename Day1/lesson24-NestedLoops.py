"""for x in range (1,10):
    print (x, end=" ") #print statement normally end with a newline character .as we need to print them in the same line we end it with a space

"""
"""
for y in range(3):
    for x in range (1,10):
        print (x, end=" ")
    print() #used to beak a inner loop to a another line

"""

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()



