# function is a group of statements performing a specific task. 

# Function definition
def avg():
    a = int(input("Ebter a number: "))
    b = int(input("Ebter a number: "))
    c = int(input("Ebter a number: "))

    avg = (a+b+c)/3
    print(avg)

# #Function call
avg()

# Quick Quiz
def greet():
    name = input("Enter your name: ")
    print(f"Hello {name} !!")

greet()