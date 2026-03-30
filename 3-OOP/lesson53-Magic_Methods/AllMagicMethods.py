# Define a class
class Student:

    # ==============================
    # OBJECT LIFECYCLE METHODS
    # ==============================

    # Constructor (called automatically when object is created)
    def __init__(self, name, gpa):
        self.name = name      # Student name
        self.gpa = gpa        # Student GPA

    # Destructor (called when object is deleted)
    def __del__(self):
        print(f"{self.name} object deleted")


    # ==============================
    # STRING REPRESENTATION METHODS
    # ==============================

    # User-friendly string (used with print())
    def __str__(self):
        return f"Student: {self.name}, GPA: {self.gpa}"

    # Developer-friendly representation (used with repr())
    def __repr__(self):
        return f"Student('{self.name}', {self.gpa})"


    # ==============================
    # COMPARISON OPERATORS
    # ==============================

    # Equal (==)
    def __eq__(self, other):
        return self.gpa == other.gpa

    # Not equal (!=)
    def __ne__(self, other):
        return self.gpa != other.gpa

    # Greater than (>)
    def __gt__(self, other):
        return self.gpa > other.gpa

    # Less than (<)
    def __lt__(self, other):
        return self.gpa < other.gpa

    # Greater than or equal (>=)
    def __ge__(self, other):
        return self.gpa >= other.gpa

    # Less than or equal (<=)
    def __le__(self, other):
        return self.gpa <= other.gpa


    # ==============================
    # ARITHMETIC OPERATORS
    # ==============================

    # Addition (+) → combine GPA values
    def __add__(self, other):
        return self.gpa + other.gpa

    # Subtraction (-)
    def __sub__(self, other):
        return self.gpa - other.gpa

    # Multiplication (*)
    def __mul__(self, other):
        return self.gpa * other.gpa

    # Division (/)
    def __truediv__(self, other):
        return self.gpa / other.gpa


    # ==============================
    # BUILT-IN FUNCTION SUPPORT
    # ==============================

    # len(object) → returns length of name
    def __len__(self):
        return len(self.name)

    # bool(object) → evaluates truth value
    def __bool__(self):
        return self.gpa > 0


    # ==============================
    # CALLABLE OBJECT
    # ==============================

    # Allows object to be called like a function
    def __call__(self):
        return f"{self.name} is being called like a function!"


    # ==============================
    # ATTRIBUTE HANDLING
    # ==============================

    # Called when attribute is not found
    def __getattr__(self, item):
        return f"'{item}' attribute not found"

    # Called whenever attribute is set
    def __setattr__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setattr__(key, value)


    # ==============================
    # INDEXING SUPPORT (LIKE DICTIONARY)
    # ==============================

    # Access like obj["name"]
    def __getitem__(self, key):
        return getattr(self, key)

    # Assign like obj["gpa"] = 3.5
    def __setitem__(self, key, value):
        setattr(self, key, value)


    # ==============================
    # CONTEXT MANAGER SUPPORT
    # ==============================

    # Runs at start of 'with' block
    def __enter__(self):
        print("Entering context")
        return self

    # Runs at end of 'with' block
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")


# ==============================
# TESTING THE CLASS
# ==============================

# Create objects
s1 = Student("Spongebob", 3.2)
s2 = Student("Patrick", 2.1)

# String methods
print(s1)                # __str__
print(repr(s1))          # __repr__

# Comparison
print("s1 > s2 :", s1 > s2)
print("s1 < s2 :", s1 < s2)
print("s1 == s2 :", s1 == s2)

# Arithmetic
print("Combined GPA:", s1 + s2)

# Built-in functions
print("Length of name:", len(s1))
print("Boolean value:", bool(s1))

# Callable object
print(s1())

# Attribute handling
print(s1.age)            # __getattr__ (not found)

# Dictionary-like access
print(s1["name"])        # __getitem__
s1["gpa"] = 3.8          # __setitem__
print(s1)

# Context manager
with s1 as student:
    print(student)