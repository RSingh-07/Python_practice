class Employee:
    a = 1
    @classmethod   #is a mehtod which is bound to the class and not the object of the class
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 45  

e.show()