import os

# Relative = folder/test.txt
# Absolute = C:/Users/sahan/Desktop/test.txt

file_path1 = "text.txt"
file_path2 = "testFiles/testFile1.txt"
file_path3 = "C:/Users/sahan/OneDrive/Desktop/PythonFileTest.txt"
file_path4 = "C:/Users/sahan/OneDrive/Desktop/PythonFileTest.txt"

print("------------------ Relative Path - File1 ------------------\n")

if os.path.exists(file_path1):
    print(f"The location '{file_path1}' exists")
else:
    print("That Location doesnt exist.")


print("\n------------------ Relative Path - File2 ------------------\n")

if os.path.exists(file_path2):
    print(f"The location '{file_path2}' exists")
else:
    print("That Location doesnt exist.")


print("\n------------------ Absolute Path - File3 ------------------\n")

#first You have to create a Desktop Text File in your device as PythonFileTest.txt


if os.path.exists(file_path3):
    print(f"The locations '{file_path3}' exists")
else:
    print("That Location doesnt exist.")

print("\n------------------ File or Folder check - File4 ------------------\n")

if os.path.exists(file_path4):
    print(f"The locations '{file_path4}' exists")

    #*Checking if it is a file or a directory
    if os.path.isfile(file_path4):
        print("This is a file 📄")
    elif os.path.isdir(file_path4):
        print("This is a Folder. 📁")

else:
    print("That Location doesnt exist.")


