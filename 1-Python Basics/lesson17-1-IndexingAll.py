# ==============================
# PYTHON INDEXING & SLICING GUIDE
# ==============================

# We will use strings, lists, and nested lists

# --------------------------------
# 1. BASIC INDEXING
# --------------------------------
text = "PYTHON"
nums = [10, 20, 30, 40, 50]

print(text[0])     # First character -> P
print(text[3])     # Fourth character -> H
print(text[-1])    # Last character -> N
print(nums[-2])    # Second last number -> 40


# --------------------------------
# 2. BASIC SLICING (start:stop)
# --------------------------------
print(text[0:4])   # From index 0 to 3 -> PYTH
print(text[:3])    # Start omitted -> PYT
print(text[3:])    # End omitted -> HON
print(text[:])     # Full copy -> PYTHON


# --------------------------------
# 3. STEP SLICING (start:stop:step)
# --------------------------------
numbers = [0, 1, 2, 3, 4, 5, 6]

print(numbers[::2])    # Every 2nd element -> [0, 2, 4, 6]
print(numbers[1::2])   # Start at index 1, step 2 -> [1, 3, 5]
print(text[::2])       # Every 2nd letter -> PTO


# --------------------------------
# 4. REVERSE A SEQUENCE
# --------------------------------
print(text[::-1])      # Reverse string -> NOHTYP
print(numbers[::-1])   # Reverse list


# --------------------------------
# 5. NEGATIVE INDEX SLICING
# --------------------------------
print(text[-4:-1])     # From -4 to -2 -> THO
print(text[:-2])       # All except last 2 -> PYTH
print(text[-3:])       # Last 3 letters -> HON


# --------------------------------
# 6. OUT-OF-RANGE SAFE SLICING
# --------------------------------
small = "HI"

print(small[0:10])     # No error -> HI
print(small[-10:2])    # No error -> HI


# --------------------------------
# 7. NESTED INDEXING
# --------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])        # First row -> [1, 2, 3]
print(matrix[1][2])     # Row 2, Col 3 -> 6
print(matrix[-1][-1])   # Last row, last col -> 9


# --------------------------------
# 8. USING len() WITH INDEXING
# --------------------------------
items = ['a', 'b', 'c', 'd', 'e']

print(items[len(items) - 1])   # Last item -> e
print(items[len(items) // 2])  # Middle item -> c


# --------------------------------
# 9. MODIFYING LISTS WITH INDEX
# --------------------------------
arr = [10, 20, 30]

arr[1] = 99          # Change value at index 1
print(arr)           # [10, 99, 30]


# --------------------------------
# 10. MODIFYING LISTS WITH SLICING
# --------------------------------
arr = [1, 2, 3, 4, 5]

arr[1:4] = [20, 30, 40]   # Replace part of list
print(arr)                 # [1, 20, 30, 40, 5]


# --------------------------------
# 11. COMMON PRACTICAL PATTERNS
# --------------------------------
sample = [100, 200, 300, 400, 500]

print(sample[0])      # First element
print(sample[-1])     # Last element
print(sample[1:])     # All except first
print(sample[:-1])    # All except last
print(sample[:])      # Copy of list
print(sample[::-1])   # Reversed list
print(sample[::2])    # Every 2nd element
print(sample[len(sample)//2])  # Middle element


# --------------------------------
# 12. INDEX ERROR VS SAFE SLICING
# --------------------------------
test = [1, 2, 3]

# print(test[5])  # Uncommenting this line causes IndexError

print(test[0:10])   # Safe slicing -> [1, 2, 3]


# --------------------------------
# 13. STRINGS ARE IMMUTABLE
# --------------------------------
word = "HELLO"

# word[0] = "Y"   # ❌ This would cause TypeError

# Instead, create a new string
new_word = "Y" + word[1:]
print(new_word)     # YELLO


# --------------------------------
# 14. TUPLES (READ-ONLY INDEXING)
# --------------------------------
t = (10, 20, 30)

print(t[1])      # Works -> 20
# t[1] = 99      # ❌ TypeError (tuples are immutable)


# ==============================
# END OF INDEXING DEMONSTRATION
# ==============================
