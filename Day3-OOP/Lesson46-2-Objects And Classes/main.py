from car import Car  #in here we import the Car class from car.py file

car1 = Car("Ford Mustang",2025,"Grey")
car2 = Car("Corvette",2025,"Blue")
car3 = Car("Ferrari",2025,"Red")

print(F"Car 1 Model: {car1.model}")
print(F"Car 1 Year: {car1.year}")
print(F"Car 1 Color: {car1.color}")
print(f"car 1 is a {car1.model} which was made in {car1.year} and is {car1.color} color.")

print("\n-----------------------------\n")

print(F"Car 2 Model: {car2.model}")
print(F"Car 2 Year: {car2.year}")
print(F"Car 2 Color: {car2.color}")
print(f"car 2 is a {car2.model} which was made in {car2.year} and is {car2.color} color.")

print("\n-----------------------------\n") 

print(F"Car 3 Model: {car3.model}")
print(F"Car 3 Year: {car3.year}")
print(F"Car 3 Color: {car3.color}")
print(f"car 3 is a {car3.model} which was made in {car3.year} and is {car3.color} color.")

print("\n-----------------------------\n")
