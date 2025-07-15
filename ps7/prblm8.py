n = int(input("Enter a number: "))

for i in range(1,n+1):
    print("*"*i)

'''
For n = 3
*
**
***

'''   



n = int(input("Enter a number: "))

for i in range(1,n+1):
    print("*"*((n+1)-i))
    


'''
For n = 3

***
**
*

'''
