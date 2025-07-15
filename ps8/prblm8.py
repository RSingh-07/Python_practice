def table(n):
   for i in range(1,11):
        result = (f"{n} X {i} = {n*i}") 
        return result
      


n = int(input("Enter a number: "))
print(table(n))