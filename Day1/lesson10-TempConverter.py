temp=float(input("Enter the Temperature : "))
unit=input("What is the Unit to be converted 'C' or 'F' : ")

if unit=='F':
    temp = round((temp * 9/5) + 32,2)
    print(f"Temperature in Farenheit is {temp} ")
elif unit=='C':
    temp = round((temp - 32) * 5/9,2)
    print(f"Temperature in Celsius is {temp} ")
else:
    print("Invalid Unit")

