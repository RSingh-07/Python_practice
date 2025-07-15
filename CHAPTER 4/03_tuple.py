a = (1, 2, 5, 6)
print(type(a))  # collections but immutable

# empty tuple
b = ()
# int 
b = (1)
# tuple with one element 
b =(1,)

c = (1, 45, 342, 3424, False, 45, "Rohan", "Riya")
#a[0] = 453  #TypeError: 'tuple' object does not support item assignment


no = c.count(45)
print(no)