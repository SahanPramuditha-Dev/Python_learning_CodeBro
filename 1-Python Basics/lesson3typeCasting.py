#Typecasting= process of converting one data type to another data type

        #str()= converts to string data type
        #int()= converts to integer data type
        #float()= converts to float data type
        #bool()= converts to boolean data type        

name = "Sahan"
age = 22
birth_year = 2003
weight = 90.5
is_married = True

print(type(name))          #<class 'str'>
print(type(age))           #<class 'str'>
print(type(birth_year))    #<class 'int'>
print(type(weight))        #<class 'float'>
print(type(is_married))    #<class 'bool'>

print("\n######################################################\n")
print("converting to data types")

weight = int(weight)  #float to int
print(type(weight))   #<class 'int'>
print(weight)        #90

age =float(age)
print(type(age))    #<class 'float'>
print(age)          #22.0


print("\n######################################################\n")

print ("Errors")
#cant convert string to int or float

age =str(age)
age += "1"
print(age)         #22.01  


name = bool(name)
print(type(name))   #<class 'bool'>
print(name)         #True If string is not empty it returns True

# More Examples
num1 = ""
num2 = "Sahan"

num1 = bool(num1)
print(num1)          #False  If string is empty it returns False

num2 = bool(num2)
print(num2)          #True


num1

