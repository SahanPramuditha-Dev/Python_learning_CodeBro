#Class Variables = Shared among all instances of a class
#                   Defined outside the construtor
#                   Allow you to share data among all objects created from that class 


class Student:

    grad_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1 # 


student1 = Student("Sahan",25)
student2 = Student("Lucifer",100)
student3 = Student("Chloe", 30)

print(f"Student 1's name is {student1.name} and he/her age is {student1.age} years")
print(f"Student 2's name is {studnt2.name} and he/her age is {studnt2.age} years")


print("\n-----------------------------\n")

print(f"Student 1's graduation year is {student1.grad_year}")
print(f"Student 2's graduation year is {student2.grad_year}")

print("\n-----------------------------\n")

# Printing Class variable

print(f"Students grad_year is {Student.grad_year}")

print("\n-----------------------------\n")

print(f"Number of students is {Student.num_students}")

print("\n-----------------------------\n")


