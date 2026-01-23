friends = 0

print("\nArithmetic Operations")

print("\nAddition\n")

friends = friends + 1
print(friends)
friends += 1
print(friends)

print("\nSubtraction\n")
friends -=1
print(friends)


print("\nMultiplication\n")
friends *= 2
print(friends)

print("\nDivision\n")
friends /= 2
print(friends)

print("\nFloor Division\n")
friends //= 2
print(friends)

print("\nModulus\n")
remainder = 10 % 3
print(remainder)

print("\nExponentiation\n")
squared = 3 ** 2
print(squared)

#Operator Precedence

print("\nOperator Precedence\n")

print ("operator precedence is as follows:")
print("1. Parentheses ()")
print("2. Exponentiation **")
print("3. Multiplication * , Division / , Floor Division // , Modulus %")
print("4. Addition + , Subtraction -")

print("\nExamples:\n")

result = 3 + 5 * 2
print(result)  #13

result = (3 + 5) * 2
print(result)  #16
# --- IGNORE ---
result = 10 - 2 ** 3 + 4 / 2
print(result)  # -2.0
result = 10 - (2 ** 3) + (4 / 2)
print(result)  # -2.0
result = (10 - 2) ** (3 + 4) / 2
print(result)  # 4096.0
# --- IGNORE ---
result = 10 - 2 ** (3 + 4) / 2
print(result)  # -78.0
# --- IGNORE ---
result = (10 - 2 ** 3 + 4) / 2
print(result)  # 3.0

