# Python String Methods – Complete Examples Script with Explanations

print("🔤 Case Conversion")
text = "hello world"
print(text.lower())        # Converts all characters to lowercase
print(text.upper())        # Converts all characters to uppercase
print(text.title())        # Capitalizes the first letter of each word
print(text.capitalize())   # Capitalizes only the first letter of the string
print("HeLLo".swapcase())  # Swaps uppercase to lowercase and vice versa
print("ß".casefold())      # Aggressive lowercase conversion (used for comparisons)

print("\n🔍 Searching & Finding")
text = "banana"
print(text.find("na"))        # Returns first index of 'na' (or -1 if not found)
print(text.rfind("na"))       # Returns last index of 'na'
print(text.index("ba"))       # Like find(), but raises error if not found
print(text.rindex("na"))      # Last occurrence, raises error if not found
print(text.count("na"))       # Counts how many times 'na' appears
print(text.startswith("ban")) # Checks if string starts with 'ban'
print(text.endswith("na"))    # Checks if string ends with 'na'

print("\n✂️ Modifying & Replacing")
text = "  hello python  "
print(text.replace("python", "world"))  # Replaces 'python' with 'world'
print(text.strip())     # Removes spaces from both ends
print(text.lstrip())    # Removes spaces from the left side
print(text.rstrip())    # Removes spaces from the right side
print("unhappy".removeprefix("un"))      # Removes 'un' from the start
print("file.txt".removesuffix(".txt"))   # Removes '.txt' from the end

print("\n🧩 Splitting & Joining")
text = "apple,banana,grape"
print(text.split(","))          # Splits string into list using comma
print(text.rsplit(",", 1))      # Splits from right side, only once
print("line1\nline2".splitlines())  # Splits at line breaks
print("-".join(["2026","01","27"]))  # Joins list into string with '-'
print("key=value".partition("="))    # Splits into 3 parts at first '='
print("key=value=test".rpartition("=")) # Splits at last '='

print("\n📏 Alignment & Formatting")
print("cat".center(7))      # Centers text in width of 7
print("cat".ljust(7))       # Left-aligns text in width of 7
print("cat".rjust(7))       # Right-aligns text in width of 7
print("42".zfill(5))        # Pads with zeros on the left
print("My name is {}".format("Sahan"))  # Inserts value into placeholder
print("{name} is {age}".format_map({"name": "Sam", "age": 20}))  # Uses dictionary for formatting

print("\n🔡 Character Type Checks")
print("abc123".isalnum())   # True if only letters and numbers
print("abc".isalpha())      # True if only letters
print("hello".isascii())    # True if all characters are ASCII
print("123".isdigit())      # True if all digits
print("123".isdecimal())    # True if all decimal characters
print("½".isnumeric())      # True if numeric (includes fractions, Roman numerals)
print("abc".islower())      # True if all letters are lowercase
print("ABC".isupper())      # True if all letters are uppercase
print("Hello World".istitle())  # True if each word starts with uppercase
print("   ".isspace())      # True if string contains only whitespace
print("Hello!".isprintable())   # True if all characters are printable
print("variable_1".isidentifier())  # True if valid Python variable name

print("\n🔁 Encoding & Translation")
print("hello".encode("utf-8"))   # Converts string into bytes
table = str.maketrans("aeiou", "*****")  # Creates translation table
print("education".translate(table))      # Replaces vowels using table

print("\n🧵 Miscellaneous")
print("hello\tworld".expandtabs(4))  # Replaces tab with spaces
print("Hello " + "World")            # Concatenation (joins strings)
print("H" in "Hello")                # Checks if 'H' exists in string
print(len("Hello"))                  # Returns length of string
