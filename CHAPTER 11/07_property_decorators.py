class Employee:
    a = 1
    @classmethod   #is a mehtod which is bound to the class and not the object of the class
    # to access or modify class-level data
    def show(cls):  # prints class variable a
        print(f"The class value of a is {cls.a}")

    @property  # Turns a method into an attribute-like access.
    # To get a value as if you're accessing a variable, not calling a method.
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter #Lets you set the property like a normal variable.
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45 

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()