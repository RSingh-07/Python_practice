a = int(input("Enter a number: "))
b =int(input("Enter second number: "))

try:
    print(f"The division of {a} and {b} gives {a/b}")
except ZeroDivisionError:
    print("Infinite")