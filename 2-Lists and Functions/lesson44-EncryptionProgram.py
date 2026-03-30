import random
import string

# --------------------------------------------------
# STEP 1: Define the character set
# --------------------------------------------------
# This includes:
# - whitespace (space, tab, newline)
# - punctuation (!@#$%^&* etc.)
# - digits (0–9)
# - uppercase and lowercase letters (A–Z, a–z)
chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters

# Convert the character string into a list so it can be indexed
chars = list(chars)

# --------------------------------------------------
# STEP 2: Generate a substitution key
# --------------------------------------------------
# Create a copy of the original character list
# This copy will be shuffled to create the encryption key
key = chars.copy()

# Randomly shuffle the key list
# Each character in 'chars' now maps to a random character in 'key'
random.shuffle(key)

# --------------------------------------------------
# STEP 3: Encryption
# --------------------------------------------------
# Get plaintext input from the user
plaintext = input("Enter the text to encrypt: ")

# Variable to store encrypted output
ciphertext = ""

# Encrypt each character
for letter in plaintext:
    # Find the index of the character in the original list
    index = chars.index(letter)

    # Use the same index to get the encrypted character from the key
    ciphertext += key[index]

# Display encryption results
print(f"\nOriginal text  : {plaintext}")
print(f"Encrypted text : {ciphertext}")

# --------------------------------------------------
# STEP 4: Decryption
# --------------------------------------------------
# IMPORTANT:
# We must use a NEW variable.
# Reusing 'plaintext' would cause incorrect output.
decrypted_text = ""

# Decrypt each character
for letter in ciphertext:
    # Find the index of the encrypted character in the key
    index = key.index(letter)

    # Use the same index to retrieve the original character
    decrypted_text += chars[index]

# Display decryption results
print(f"Decrypted text : {decrypted_text}")
