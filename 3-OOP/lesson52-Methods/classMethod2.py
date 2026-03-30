# Define a class named Student
class Student:

    # Class variable
    # This variable belongs to the class itself, not individual objects
    # It will keep track of how many Student objects are created
    count = 0
    students = []


    # Constructor method
    # This runs automatically whenever a new Student object is created
    def __init__(self, name, gpa):

        # Instance variable
        # Each student object will store its own name
        self.name = name

        # Instance variable
        # Each student object will store its own GPA
        self.gpa = gpa

        # Increase the class variable 'count' every time a new student is created
        Student.count += 1

        # add each created object to the class list
        Student.students.append(self)


    # Instance method
    # This method returns information about a specific student object
    def get_info(self):

        # f-string is used for formatting output
        return f"{self.name} {self.gpa}"


    # Class method
    # This method belongs to the class, not to individual objects
    # It can access class variables
    @classmethod
    def get_count(cls): #like self for instances ,cls is for class 

        # cls refers to the class itself (Student)
        return f"Total # of Students :{cls.count}"
    
    @classmethod
    def list_names(cls):
        # iterate through stored student objects
        for student in cls.students:
            print(f"Name of the Student: {student.name}")


# Create first student object
student1 = Student("Spongebob", 3.2)

# Create second student object
student2 = Student("Patrick", 2.1)


student2 = Student("Mr.Crabs", 2.9)

# Call the class method using the class name
# This prints how many Student objects have been created
print(Student.get_count())
Student.list_names()