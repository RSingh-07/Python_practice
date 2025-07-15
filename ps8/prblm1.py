def greatest_of_three_nums(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

result = greatest_of_three_nums(a,b,c)
print(f"{result} is the greatest number")