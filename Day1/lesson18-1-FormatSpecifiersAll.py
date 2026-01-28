# ============================================
# PYTHON FORMAT SPECIFIERS & STRING FORMATTING
# ============================================

# We will cover:
# 1. % formatting (old style)
# 2. str.format() method
# 3. f-strings (modern style)
# 4. Alignment, padding, width, precision
# 5. Combined examples

# --------------------------------------------
# 1. OLD STYLE (%) FORMATTING
# --------------------------------------------
name = "Sahan"
age = 20
pi = 3.1415926

# %s → string
print("My name is %s" % name)

# %d → integer
print("I am %d years old" % age)

# %f → float (default 6 decimals)
print("Value of pi: %f" % pi)

# %.2f → float with 2 decimals
print("Pi rounded: %.2f" % pi)

# Multiple values
print("%s is %d years old and pi = %.3f" % (name, age, pi))

# Padding numbers
num = 42
print("Number padded with zeros: %05d" % num)   # 00042

# --------------------------------------------
# 2. str.format() METHOD
# --------------------------------------------
# Basic replacement
print("My name is {}".format(name))

# Positional arguments
print("{} is {} years old".format(name, age))

# Named arguments
print("{n} is {a} years old".format(n=name, a=age))

# Formatting numbers
print("Pi: {:.2f}".format(pi))       # 2 decimals
print("Number padded: {:05}".format(num))  # Zero padding

# Alignment
print("{:<10} Left aligned".format("Text"))   # Left
print("{:>10} Right aligned".format("Text"))  # Right
print("{:^10} Center aligned".format("Text")) # Center

# Combining width and precision
print("Pi with width 8 and 3 decimals: {:8.3f}".format(pi))

# --------------------------------------------
# 3. F-STRINGS (Python 3.6+)
# --------------------------------------------
# Basic f-string
print(f"My name is {name} and I am {age} years old")

# Formatting floats
print(f"Pi: {pi:.3f}")  # 3 decimals

# Alignment and padding
print(f"{'Left':<10} <- Left")
print(f"{'Right':>10} <- Right")
print(f"{'Center':^10} <- Center")

# Integer zero padding
print(f"Number with zeros: {num:05}")  # 00042

# Combined example
score = 95.6789
print(f"{name:<10} Age: {age:03} Score: {score:7.2f}")
# Output: 'Sahan      Age: 020 Score:   95.68'

# --------------------------------------------
# 4. OTHER USEFUL FORMAT SPECIFIERS
# --------------------------------------------
x = 255

# Binary, Octal, Hexadecimal
print(f"Binary: {x:b}")      # 11111111
print(f"Octal: {x:o}")       # 377
print(f"Hex (lowercase): {x:x}") # ff
print(f"Hex (uppercase): {x:X}") # FF

# Percentage formatting
ratio = 0.8567
print(f"Percentage: {ratio:.2%}")  # 85.67%

# Thousands separator
large_num = 1234567890
print(f"With comma: {large_num:,}")  # 1,234,567,890
print(f"With underscore: {large_num:_}")  # 1_234_567_890

# --------------------------------------------
# 5. FORMATTING WITH VARIABLES AND EXPRESSIONS
# --------------------------------------------
width = 10
precision = 4
value = 12.3456789

print(f"Value with dynamic width and precision: {value:{width}.{precision}f}")

# Arithmetic in f-strings
a = 5
b = 3
print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")

# --------------------------------------------
# 6. SUMMARY TABLE EXAMPLES
# --------------------------------------------
print("\nSummary of Common Format Specifiers:")
print(f"{'Specifier':<10} {'Description':<30} {'Example'}")
print(f"{'%s':<10} {'String':<30} {'print(\"Hello %s\" % \"World\")'}")
print(f"{'%d':<10} {'Integer':<30} {'print(\"%d\" % 42)'}")
print(f"{'%f':<10} {'Float':<30} {'print(\"%.2f\" % 3.14159)'}")
print(f"{'{:s}':<10} {'String (format)'} {'\"{:s}\".format(\"Hi\")'}")
print(f"{'{:.2f}':<10} {'Float 2 decimals'} {'\"{:.2f}\".format(3.14159)'}")
print(f"{'{:<10}':<10} {'Left align'} {'\"{:<10}\".format(\"Hi\")'}")
print(f"{'{:>10}':<10} {'Right align'} {'\"{:>10}\".format(\"Hi\")'}")
print(f"{'{:^10}':<10} {'Center'} {'\"{:^10}\".format(\"Hi\")'}")
print(f"{'{:05}':<10} {'Zero padded'} {'\"{:05}\".format(42)'}")
print(f"{'{:.2%}':<10} {'Percentage'} {'\"{:.2%}\".format(0.8567)'}")
