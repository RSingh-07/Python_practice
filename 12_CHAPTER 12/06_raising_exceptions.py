a = int(input("Enter a number: \n"))
b = int(input("Enter second number: \n"))

if(b==0):
    # In raise program will crash
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}\n")