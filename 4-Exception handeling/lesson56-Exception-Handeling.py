# ==============================
# PYTHON EXCEPTION HANDLING EXAMPLE
# ==============================

try:
    # Attempt to get user input and perform division
    number = int(input("Enter a number: "))
    print(1 / number)

except ZeroDivisionError:
    # Handles the case where user enters 0
    print("Division by zero is not allowed.")

except ValueError:
    # Handles the case where user enters non-numeric input
    print("Please enter a valid numeric value.")

except Exception as e:
    # Catch-all for any other unexpected exceptions
    # The exception object 'e' provides details of the error
    print(f"An unexpected error occurred: {e}")

finally:
    # This block always executes regardless of exceptions
    # Useful for cleanup operations like closing files or releasing resources
    print("Execution completed. Cleanup done if required.")