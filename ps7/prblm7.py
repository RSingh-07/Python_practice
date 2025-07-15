'''
For n=3
  *
 ***
*****

'''

n = int(input("Enter the number: "))
for i in range(1, (n+1)):
  print(" "* (n-i), end=" ") # By default, every print() statement ends with a newline (\n)
  print("*"* (2*i-1), end="") # New line (default)
  print(" ")                  # ""	Nothing (stay on same line)   
                              # " "	Add space                 
                              #  ","	Add comma                 
                              #  " - "	Custom separator

