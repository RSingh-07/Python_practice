# Write a recursive function to calculate the sum of first n natural numbers.


'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4

sum(n) = 1 + 2 + 3 + 4 + 5 + ..... + (n-1) + n
sum(n) = sum(n-1) + n

'''
def sum_of_natural_num(n):
    if(n==1):     # base condition
        return 1
    return sum_of_natural_num(n-1) + n

print(sum_of_natural_num(4))