import math

A =float(input("Enter the length of side A of the right-angled triangle: "))
B =float(input("Enter the length of side B of the right-angled triangle: "))

C = (A**2 + B**2)**0.5
# or you can use math.sqrt() function after importing math module
# C = math.sqrt(math.pow(A,2) + math.pow(B,2))
print(f"The length of the hypotenuse C is: {round(C,2)}")