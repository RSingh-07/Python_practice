class Employee:
    language = "Python" #This is a class attribute
    salary = 1200000

harry = Employee()
harry.language = "Javascript" #This is an object attribute
print(harry.language, harry.salary)


# Note: Instance attributes, take preference over class attributes during assignment & retrieval.