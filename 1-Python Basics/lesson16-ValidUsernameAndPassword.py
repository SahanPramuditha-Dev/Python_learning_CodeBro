#Valid Username
#Rules
# 1. username is max 12 characters
# 2.username must not contain space
# 3.username must Not contain digits

username = input("Enter your username: ")
length = len(username)


if length >= 12:
    print(f"Username is too long. Max length is 12 characters.You entered {length} characters")
elif " " in username:
    print("Username cannot contain spaces")
elif not username.isalpha():  # isalpha() returns True only if ALL characters are letters (A–Z, a–z). This blocks digits, spaces, and special characters
    print ("Username cannot contain digits")
else:
    print("Username Accepted as a Valid Username")

# Valid Password Checker

# Rules
# 1. Password must be at most 12 characters
# 2. Password must not contain spaces
# 3. Password must contain at least one uppercase letter
# 4. Password must contain at least one lowercase letter
# 5. Password must contain at least one digit
# 6. Password must contain at least one special character

password = input("Enter your password: ")

if len(password) > 12:
    print(f"Password is too long. Max length is 12 characters. You entered {len(password)} characters.")

elif " " in password:
    print("Password cannot contain spaces.")

elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")

elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")

elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")

elif password.isalnum():
    print("Password must contain at least one special character.")
    # isalnum() == True means only letters and digits, no symbols

else:
    print("Password accepted as a valid password.")
