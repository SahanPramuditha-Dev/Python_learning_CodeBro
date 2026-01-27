import math

w = 9
x = 3.14
y = -4
z = 5

result = math.ceil(x) #rounds up to nearest integer example 3.14 to 4
print(result)  #4

result = math.floor(x) #rounds down to nearest integer example 3.14 to 3
print(result)  #3

result = round(x) #rounds to nearest integer example 3.14 to 3
print(result)  #3

result = abs(y) #absolute value example -4 to 4
print(result)  #4

result = pow(4, 3) #4 to the power of 3 example 4*4*4
print(result)  #64

result = max(x, y, z) #finds the maximum value among the numbers
print(result)  #5

result = min(x, y, z) #finds the minimum value among the numbers
print(result)  #-4

print(math.pi)  #3.141592653589793
print(math.pi*10) #31.41592653589793
print(math.e)   #2.718281828459045

result = math.sqrt(w)
print(result)  #3.0

result = math.sqrt(16)
print(result)  #4.0
