class Employee:
    language = "Py" #This is a class attribute
    salary ="1200000"

harry = Employee()
harry.name = "Harry" #This is an object attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.language, rohan.salary)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class

