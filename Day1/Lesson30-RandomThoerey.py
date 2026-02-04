"""
HOW PYTHON GENERATES RANDOM NUMBERS

Python’s `random` module uses a Pseudo-Random Number Generator (PRNG),
not true randomness. The algorithm behind it is called the
Mersenne Twister (MT19937).
"""

import random

# ------------------------------------------------------------
# 1. SEED — Starting Point of the Random Sequence
# ------------------------------------------------------------
# The seed is the initial value used by the PRNG.
# If you use the same seed, you get the SAME sequence of numbers.

random.seed(42)  # Setting a seed makes results reproducible

print("Random number:", random.random())


# ------------------------------------------------------------
# 2. CORE IDEA OF THE ALGORITHM
# ------------------------------------------------------------
# The generator does NOT pick numbers randomly.
# Instead, it uses a deterministic formula like:
#
#     X(n+1) = f(X(n))
#
# Each new number is calculated from the previous internal state.


# ------------------------------------------------------------
# 3. MERSENNE TWISTER INTERNAL WORKING (CONCEPTUAL)
# ------------------------------------------------------------
# Python maintains an internal state of 624 large integers.
# It repeatedly updates them using bitwise math operations
# like XOR, shifts, and masks to "mix" the bits.

# Example of bitwise operations used internally (simplified idea):
x = 123456789
y = x ^ (x >> 11)   # XOR and bit shifting (similar to real tempering steps)

print("Example bitwise result:", y)


# ------------------------------------------------------------
# 4. HOW random.random() IS MADE
# ------------------------------------------------------------
# The algorithm generates a 32-bit pseudo-random integer
# Then divides it by 2^32 to produce a float between 0 and 1

rand_int = random.getrandbits(32)   # 32 pseudo-random bits
rand_float = rand_int / (2**32)

print("Generated float (0 to 1):", rand_float)


# ------------------------------------------------------------
# 5. PERIOD OF THE GENERATOR
# ------------------------------------------------------------
# The sequence length before repeating is:
#     2^19937 - 1
# This is an extremely large number, so repetition is practically impossible.


# ------------------------------------------------------------
# 6. IMPORTANT LIMITATION
# ------------------------------------------------------------
# Because this is deterministic math, if someone knows the seed
# or internal state, they can predict all future numbers.
# That is why `random` is NOT safe for passwords or security.

# For security-sensitive randomness, use:
import secrets
print("Secure random token:", secrets.token_hex(8))


"""
SUMMARY:
Python random numbers are produced by a deterministic mathematical
algorithm (Mersenne Twister) that simulates randomness using
bitwise operations and a large internal state.
"""
