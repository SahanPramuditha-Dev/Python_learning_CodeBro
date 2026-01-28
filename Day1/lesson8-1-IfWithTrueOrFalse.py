"""is_For_Sale = True
if is_For_Sale: #this statment is considered as true
    print("This item is for sale")
else:
    print("This item is not for sale")

"""
"""
value=bool(input("Do you want to confirm Your Order ? "))

if value: #if you type anything at all (like "yes", "no", "123", "abc"), it will be treated as True
    print("Your Order is Confirmed")
else: #Only if you press Enter without typing anything, it will be False
    print("Your Order is Cancelled")
"""

value = input("Do you want to confirm Your Order? ").strip().lower()

if value in ["yes", "y"]:
    print("Your Order is Confirmed")
else:
    print("Your Order is Cancelled")
