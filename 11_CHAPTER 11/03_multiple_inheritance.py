class Employee:
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder): # multiple inheritance
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good at {self.language} language.")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()