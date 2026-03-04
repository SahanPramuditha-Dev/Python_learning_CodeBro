# A Static Method is a method that belongs to a class rather than an instance (object) of that class.
# It is used for utility functions that perform a task related to the class but do not need to access or modify data specific to an individual object.

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod

    def is_valid_position(position):
        valid_postion = ["Manager","Cashier","Cook","Janitor"]
        return postion in valid_postion
    
employee1 = Employee("Eugene","Manager")



print(employee1.get_info())






















