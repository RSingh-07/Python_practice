from functools import reduce

l = [1, 2, 3, 4, 5]
def max(a,b):
    if(a>b):
        return a
    elif (b>a):
        return b
    
print(reduce(max,l))
  

