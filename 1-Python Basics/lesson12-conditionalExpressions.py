"""
num=int(input("Enter the Number to Check : "))

print("positive number" if num>0 else "negative number" if num<0 else "zero")
print("Even number" if num%2==0 else "Odd number")

"""
#Access

username = input("Enter your username: ")
password = input("Enter your password: ")
Ovveride_Code = input("Enter the System Administrative Code: ")

if Ovveride_Code == "1357":
    privilage = "Administrative"
else:
    privilage = "Standard"


print(f"Username and Password Accepted . System Access Granted .{username} , You Have {privilage} Privilages" if username == "Sahan" and password == "1234" else "Access Denied Due to Invalid Credentials.")

