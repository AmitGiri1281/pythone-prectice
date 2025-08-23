# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
        
#     def printname(self):
#         print(self.firstname, self.lastname)
# x = Person("amit", "giri")
# x.printname()



# create a child class 

# class Student(Person):
#     pass
    

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduatinyear =year
    
    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduatinyear)

