try:
    a = int(input("Enter a number: ")) #if exception not handled the prgm crashes here none of the further lines will be executed
except ValueError as v:
    print(v)
    print("heyy")
except Exception as e:
    print(e)

# When the exception is handled, the code flow continues without program interruption
print("Thank you!")