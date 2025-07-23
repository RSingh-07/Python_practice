try:
    a = int(input("Enter a number: ")) #if exception not handled the prgm crashes here none of the further lines will be executed
    print(a)
    
except Exception as e:
    print(e)

# To run a piece of code when try was successful.
else:
    print("I am inside else")

