class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good at {self.language} language.")
#INSTEAD OF DOING THIS WHICH IS ERROR PRONE AND CUMBERSOME WE USE INHERITANCE.

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language.")

a = Employee()
b = Programmer()

print(a.company, b.company)
