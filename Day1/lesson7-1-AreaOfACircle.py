import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
print(f"The Circumference of the circle with radius {radius} is: {round(circumference,2)}")

area = math.pi * math.pow(radius, 2)
print("The area of the circle with radius", radius, "is:", round(area,2))