

name =input("Enter your name: ")
age =input("Enter your age: ")
current_year =2026
# birth_year = current_year - age this will cause an error because age is a string. We need to convert it to an integer.

'''There are two ways to convert a string to an integer:
1. Using int() function
birth_year = current_year - int(age)

2. Using type casting during the calculation

age_casted = int(age)
birth_year = current_year - age_casted

'''
age_casted = int(age)
birth_year = current_year - age_casted

print (name)
print(f"Hello, {name} Welcome to Python Programming!")
print(f"Your birth year is {birth_year}.")
