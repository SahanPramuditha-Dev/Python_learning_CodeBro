# 2. Static Methods (The "Toolbox")
# These methods are like a tape measure or a calculator used by the architect. The tool is related to building houses, but the tool doesn't need to know which house you are currently working on to tell you that "12 inches = 1 foot."

# Example: A utility that converts square feet to square meters.

class House:
    @staticmethod
    # STATIC METHOD: No 'self'. It's just a math utility.
    def sqft_to_sqm(sqft):
        return sqft * 0.0929

# You don't even need a house to use this!
print(House.sqft_to_sqm(1000))