"""
name=input("What is Your Name ?")

while name=="" :
    print("Please Enter Your name")
    name=input("What is Your Name ?")

print(f"{name} Welcome Back !")
 
    """

# Ask for participant age
age = int(input("Enter your age: "))

# Loop runs while age is NOT in the valid solo range
while age < 18 or age > 65:
    print("You are not eligible to participate alone. Please come with a parent.")

    parent_age = int(input("Enter your parent's age: "))

    # Check if parent is valid
    if 18 <= parent_age <= 65:
        print("Since you are with a parent in the valid age range, you can participate in the contest.")
        break   # Exit the loop because requirement is satisfied
    else:
        print("Parent must be between 18 and 65 years old.")
        print("Please try again.\n")

    # Ask again for participant age before repeating loop
    age = int(input("Re-enter your age: "))

# If loop never ran (meaning age was valid)
if 18 <= age <= 65:
    print("You can participate alone.")

print("Thank you for participating!")

