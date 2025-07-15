class Employee:
    a = 1

class Programmer(Employee): # multilevel inheritance
    b = 2


class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # 1
# print(o.b) # gives error because no b attr in employee

o = Programmer()
print(o.a, o.b) # 1 2

o = Manager()
print(o.a, o.b, o.c)
