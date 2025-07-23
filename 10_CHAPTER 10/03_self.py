class Employee:
    language = "Python" #This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
harry.language = "Javascript" #This is an object attribute
harry.getInfo()
harry.greet()
# represented as
# Employee.getInfo(harry)



# In Python, @staticmethod is a decorator used to define a method inside a class that:

# Does NOT access instance (self) or class (cls) variables.

# Belongs to the class logically, but does not require any object or class reference to operate.