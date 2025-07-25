class Employee:
    language = "Python" #This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Harry", 1300000, "Javascript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)