# ---------------- File Modes in Python ----------------
# "r"  -> Read (default). Opens file for reading. File must exist.
# "w"  -> Write. Opens file for writing. Creates file if not exists, truncates if exists.
# "a"  -> Append. Opens file to add data at the end. Creates file if not exists.
# "x"  -> Exclusive creation. Creates a new file, fails if file exists.
# "b"  -> Binary mode. Used with other modes like "rb" or "wb".
# "t"  -> Text mode (default). Used with other modes like "rt" or "wt".
# "+"  -> Update mode (read and write), e.g., "r+", "w+", "a+"

import os
import json
import csv

# Example: Writing text to a file
text_data = "I Like Pizza."
file_path = "d:/Learning/Python_learning_CodeBro/5-File Handeling/output.txt"
employee_path = "d:/Learning/Python_learning_CodeBro/5-File Handeling/employee.txt"
actor_path = "d:/Learning/Python_learning_CodeBro/5-File Handeling/Actor.json"
series_path = "d:/Learning/Python_learning_CodeBro/5-File Handeling/Series.csv"

employees = ["Spongebob", "Squidward","Patrick"]

actor = {
    "name":"Tom Ellis",
    "played": "Lucifer",
    "series": "Lucifer",
    "age":54,
    }

series = [
    ["Series", "Year", "Rating"],
    ["Game of Thrones", "2011", "9.2"],
    ["Lucifer", "2016", "8.1"],
    ["Breaking Bad", "2008", "9.5"],
    ["Peaky Blinders", "2013", "8.8"]
]


# Using 'w' mode to write (will overwrite if file exists)
with open(file_path, "w") as file:
    file.write(text_data)  # Write the string to file
    print(f"text file {file_path} was created")


#* Employees
with open(employee_path, "w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print(f"text file {employee_path} was created")

#*Actor
with open(actor_path,"w") as file:
    json.dump(actor,file, indent = 4) # turn dictionary to a json string | an indent is also added by indent = 4 for easy reading
    print(f"text file {actor_path} was created")

#* Series
with open(series_path,"w",newline = "") as file:
    writer = csv.writer(file)
    for one in series:
        writer.writerow(one)
    print(f"text file {series_path} was created")


try:
    # Using 'x' create a file
    with open(file_path, "x") as file:
        file.write(text_data)  # Write the string to file
        print(f"text file {file_path} was created")
except FileExistsError:
    print("That File already Exists")




# Using 'a' mode to append more text
with open(file_path, "a") as file:
    file.write("\nI also like pasta.")  # Adds a new line without overwriting

# Using 'r' mode to read the file
with open(file_path, "r") as file:
    content = file.read()
    print(content)