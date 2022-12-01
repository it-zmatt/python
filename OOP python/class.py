# A Class is like an object constructor, or a "blueprint" for creating objects.

# Class can't be empty, if  for some reason we need a class with no content, put Pass statement
class example:
    pass

# All  classes have the __init__() function, to assign values to object's properties
# self reference to the current class parameters
class student:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID
    
    def changeName(self):
        return self.name + "ABC"

# Creating object, and assigning values
student1 = student("Matt", 21, 2930)

# Printing the values
print(student1.name)
print(student1.changeName())