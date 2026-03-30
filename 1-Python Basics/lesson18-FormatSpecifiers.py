#Format Specifiers

price1 = 3.14159
price2 = -1987.65
price3 = 12.34
price4 = 1535546846164.05

print(f"Price 1 is ${price1:.2f}") #show upto 2 decimal points
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.5f}")

print("\n------------------------------------\n")

print(f"Price 1 is ${price1:2}") #have space upto 2 points
print(f"Price 2 is ${price2:15}")
print(f"Price 3 is ${price3:025}") #add 0 till 25 chracters including the numbers

print("\n-------------------\n")

print(f"Price 1 is ${price1:<10}") #left justified
print(f"Price 2 is ${price2:>10}") #right justified
print(f"Price 3 is ${price3:^10}") #center justified

print("\n-------------------\n")
print(f"Price 1 is ${price1:+}") #Any number is preceded with a + sign 
print(f"Price 2 is ${price2:+}") #AnEven if we add a + sign a negative number wil always show a negative sign
print(f"Price 3 is ${price3:+}")

print("\n-------------------\n")
print(f"Price 4 is ${price4:,}") # , is thousand separator
print(f"Price 2 is ${price2:,.4f}") # we can do combinations too
print(f"Price 3 is ${price3:+}")

