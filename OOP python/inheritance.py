# Inheritance allow us to inherite all properties from parent class
# Creating a Class
class person:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID
    
    def printInfo(self):
        print(self.name, self.age, self.ID)

# Creating a Child class (student) that inherits from Parent class (person)
class student(person):
    
    # Override of the __innit__ function
    def __init__(self, name, age, ID, field):

        # super function will make the child class inherit all the methods and properties from its parent
        super().__init__(name, age, ID)
        self.field = field


s = student("Matt", 21, 232)
s.printInfo()
