# Escape Sequences Demonstration Program

print("1. Backslash: C:\\Users\\Student")

print("\n2. Single Quote: It\'s a beautiful day")

print("\n3. Double Quote: She said \"Python is powerful!\"")

print("\n4. New Line:\nThis is line one\nThis is line two")

print("\n5. Tab Space:\nName:\tSahan\nAge:\t21\nCity:\tColombo")

print("\n6. Carriage Return Example (overwrites line)")
print("Hello World!\rHi")

print("\n7. Backspace Example")
print("Helloo\b!")  # removes one 'o'

print("\n8. Form Feed Example")
print("Hello\fWorld")

print("\n9. Vertical Tab Example")
print("Hello\vWorld")

print("\n10. Octal Value Example (\\101 = A)")
print("\101")

print("\n11. Hexadecimal Value Example (\\x41 = A)")
print("\x41")

print("\n12. Raw String (escape sequences ignored)")
print(r"C:\new_folder\test\nThis will NOT go to a new line")
