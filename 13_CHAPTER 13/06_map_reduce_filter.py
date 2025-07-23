from functools import reduce

# Map example
# Map applies a function to all the items in an input_list.
l = [1, 2, 3, 4, 5, 6]

square = lambda x : x*x

sqList = map(square, l)
# Returns a map object (iterator), not a list — so you often need to wrap it with list(...).
print(list(sqList))


# Use map() when:

# You want a functional approach

# You're working with built-in functions or want to chain operations cleanly


# Filter example
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#Reduce Example
def sum(a, b):
    return a+b

print(reduce(sum, l))