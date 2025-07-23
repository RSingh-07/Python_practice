class Class:
    a = 4  #class variable (shared by all instances unless overridden)

o = Class() # creates an obj o of Class
print(o.a) # 4  - prints class attr since instance attr not present

o.a = 0  # This creates a new instance variable 'a' inside object 'o'.

print(o.a) # 0 - a exists in obj itself

print(Class.a) # 4 - The original class variable a is still unchanged in the class.
                     # o.a does not affect Class.a.
