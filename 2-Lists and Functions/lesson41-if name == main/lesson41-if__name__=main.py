# ============================================================
# if __name__ == "__main__"  — FULL EXPLANATION
# ============================================================
#
# In Python, every file (module) has a built-in variable called __name__.
#
# Python automatically sets the value of __name__ depending on how
# the file is used.
#
# ------------------------------------------------------------
# CASE 1: When the file is run DIRECTLY
# ------------------------------------------------------------
# Example:
#     python my_program.py
#
# Python sets:
#     __name__ = "__main__"
#
# This means the file is the starting point of execution.
#
# Any code inside:
#     if __name__ == "__main__":
# will be executed.
#
# ------------------------------------------------------------
# CASE 2: When the file is IMPORTED
# ------------------------------------------------------------
# Example:
#     import my_program
#
# Python sets:
#     __name__ = "my_program"
#
# In this case, the condition:
#     if __name__ == "__main__":
# becomes FALSE.
#
# Therefore, the code inside this block will NOT run.
#
# ------------------------------------------------------------
# WHY THIS IS IMPORTANT
# ------------------------------------------------------------
# 1. Prevents unwanted execution when a file is imported
# 2. Allows the same file to be used as both:
#    - a reusable module
#    - a standalone program
# 3. Makes code clean, modular, and professional
# 4. Essential for large projects, testing, and libraries
#
# ------------------------------------------------------------
# CORRECT SYNTAX (IMPORTANT)
# ------------------------------------------------------------
# if __name__ == "__main__":
#     main()
#
# ------------------------------------------------------------
# COMMON MISTAKES
# ------------------------------------------------------------
# if __name__ = __main__      ❌ Wrong (assignment, not comparison)
# if __name__ == __main__    ❌ Wrong (__main__ must be a string)
# if __name__ == "__main__"  ❌ Wrong (missing colon)
#
# ------------------------------------------------------------
# STANDARD BEST PRACTICE
# ------------------------------------------------------------
# Define all functions above,
# and put only the execution logic inside the main guard.
#
# Example:
#
# def main():
#     print("Program started")
#
# if __name__ == "__main__":
#     main()
#
# ------------------------------------------------------------
# SHORT RULE TO REMEMBER
# ------------------------------------------------------------
# Code inside the main guard runs ONLY when the file
# is executed directly, NOT when it is imported.
#
# ============================================================
