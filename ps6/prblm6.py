marks =  int(input("Enter marks: "))

if(marks>=90 and marks<=100):
    print("Grade is E.", marks)
elif(marks>=80 and marks<=90):
    print("Grade is A.", marks)
elif(marks>=70 and marks<=80):
    print("Grade is B.", marks)
elif(marks>=60 and marks<=70):
    print("Grade is C.", marks)
elif(marks>=50 and marks<=600):
    print("Grade is D.", marks)
elif(marks<50 and marks>=0):
    print("Fail.", marks)
else:
    print("Invalid marks")