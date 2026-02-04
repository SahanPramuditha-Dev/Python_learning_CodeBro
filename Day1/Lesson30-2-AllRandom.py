import random
import secrets  # For secure randomness

# ------------------------------------------------------------
# 1️⃣ Basic Random Numbers
# ------------------------------------------------------------
print("Random float 0.0 <= x < 1.0:", random.random())
print("Random float between 5 and 10:", random.uniform(5, 10))
print("Random integer between 1 and 6:", random.randint(1, 6))
print("Random number from range 0-10 step 2:", random.randrange(0, 10, 2))

# ------------------------------------------------------------
# 2️⃣ Working With Sequences
# ------------------------------------------------------------
fruits = ["apple", "banana", "mango", "orange"]

print("Random choice from list:", random.choice(fruits))
print("Random 3 choices with replacement:", random.choices(fruits, k=3))
print("Random 3 unique items:", random.sample(fruits, k=3))

random.shuffle(fruits)  # Shuffles list in-place
print("Shuffled list:", fruits)

# ------------------------------------------------------------
# 3️⃣ Bits & Bytes
# ------------------------------------------------------------
print("Random 8-bit integer:", random.getrandbits(8))
# random.randbytes(n) available in Python 3.9+
if hasattr(random, "randbytes"):
    print("Random 5 bytes:", random.randbytes(5))

# ------------------------------------------------------------
# 4️⃣ Seed & State Control
# ------------------------------------------------------------
random.seed(42)  # Makes outputs reproducible
print("Random after seed:", random.random())

state = random.getstate()  # Save internal state
print("Random using saved state:", random.random())
random.setstate(state)  # Restore state
print("Random after restoring state:", random.random())

# ------------------------------------------------------------
# 5️⃣ Probability Distributions
# ------------------------------------------------------------
print("Uniform 1-10:", random.uniform(1, 10))
print("Gaussian (mu=0, sigma=1):", random.gauss(0, 1))
print("Normal (mu=0, sigma=1):", random.normalvariate(0, 1))
print("Exponential (lambda=1):", random.expovariate(1))
print("Gamma (alpha=2, beta=2):", random.gammavariate(2, 2))
print("Beta (alpha=2, beta=5):", random.betavariate(2, 5))
print("Lognormal (mu=0, sigma=1):", random.lognormvariate(0, 1))
print("Triangular (low=0, high=10, mode=5):", random.triangular(0, 10, 5))
print("Von Mises (mu=0, kappa=4):", random.vonmisesvariate(0, 4))
print("Pareto (alpha=2):", random.paretovariate(2))
print("Weibull (alpha=1, beta=2):", random.weibullvariate(1, 2))

# ------------------------------------------------------------
# 6️⃣ SystemRandom (OS-level randomness)
# ------------------------------------------------------------
secure_rand = random.SystemRandom()
print("Secure random int 1-10:", secure_rand.randint(1, 10))

# ------------------------------------------------------------
# 7️⃣ Cryptographically Secure Randomness
# ------------------------------------------------------------
print("Secure random token (hex):", secrets.token_hex(8))

# ------------------------------------------------------------
# ✅ Summary:
# random module = simulations, games, shuffling, stats
# SystemRandom or secrets = secure randomness for passwords/tokens
# ------------------------------------------------------------
