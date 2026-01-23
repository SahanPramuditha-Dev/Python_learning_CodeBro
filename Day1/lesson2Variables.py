#Variables in Python

first_name = "Sahan"
food = "Pizza"
age = 21

print(f"Hello,{first_name}.\nYour age is {age}. \nYou like {food}.")

#Strings
last_name = 'Perera'
email = "sahanpramuditha91@gmail.com"

print(f"Your last name is {last_name}.")
print(f"Your email is {email}.")

# Integer
age = 22
year = 2003
month = 9

print(f"You were born in year {year} month {month}. So now you are {age} years old.")

#float
price = 199.99
weight = 70.5

print(f"The price of the item is ${price}. Your weight is {weight} kg.")

#Boolean
is_student = True
has_license = False
do_smoking = False

print(f"Are you a student? {is_student}. Do you have a license? {has_license}.")

if do_smoking:
    print("You smoke.")
else:
    print("You don't smoke.")

#ways of printing variables
#example 1

print(f"Hello, {first_name} Welcome to Python Programming!")
print("Hello, {} Welcome to Python Programming!".format(first_name))
print("Hello, %s Welcome to Python Programming!" %first_name)
print("Hello, " + first_name + " Welcome to Python Programming!")
print("Hello,", first_name, "Welcome to Python Programming!")

print ("\n######################################################\n")

#example 2

print("Hello, {}. Your age is {}. You like {}.".format(first_name, age, food))
print("Hello, %s. Your age is %d. You like %s." %(first_name, age, food))
print("Hello, " + first_name + ". Your age is " + str(age) + ". You like " + food + ".")
print("Hello,", first_name, ". Your age is", age, ". You like", food, ".")
print(f"Hello, {first_name}. Your age is {age}. You like {food}.")



