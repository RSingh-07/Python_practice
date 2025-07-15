class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee): # multilevel inheritance
    def __init__(self):
        print("Constructor of Programmer")
    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()  #super() is used to call the parent class’s constructor.
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # 1

# o = Programmer()
# print(o.a, o.b) # 1 2

o = Manager()
print(o.a, o.b, o.c)


# Use super() consistently in all child classes to call the full inheritance chain.