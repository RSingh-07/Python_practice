l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def divisible_by_5(n):
    if(n%5==0):
        return n

multiple_of_5 = filter(divisible_by_5, l)
print(list(multiple_of_5))