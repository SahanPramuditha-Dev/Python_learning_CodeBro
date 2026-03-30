
import os
import json
import csv

text_filePath = "D:/Learning/Python_learning_CodeBro/5-File Handeling/output.txt"
json_filePath = "D:/Learning/Python_learning_CodeBro/5-File Handeling/Actor.json"
csv_filePath = "D:/Learning/Python_learning_CodeBro/5-File Handeling/Series.csv"


#*Text file reading

print("------------------ Text File ------------------\n")


try:
    with open(text_filePath,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    file_name = os.path.basename(text_filePath)
    print(f"The {file_name} was not found in the file path")

except PermissionError:
    print("You do not have permission to read that file. ")

#*Json File reading
print("\n------------------ Json File ------------------\n")


try:
    with open(json_filePath,"r") as file:
        content = json.load(file)
        print(content)
        print(content["name"]) #get a exact value
except FileNotFoundError:
    file_name = os.path.basename(json_filePath)
    print(f"The {file_name} was not found in the file path")

except PermissionError:
    print("You do not have permission to read that file. ")


#*CSV File reading

print("\n------------------ Csv File ------------------\n")


try:
    with open(csv_filePath,"r") as file:
        content = csv.reader(file) #memory address is geiven
        for line in content:
            print(line)
        print(f"Printing Line 0: {line[0]}")    
except FileNotFoundError:
    file_name = os.path.basename(csv_filePath)
    print(f"The {file_name} was not found in the file path")

except PermissionError:
    print("You do not have permission to read that file. ")








