
def convert_f_to_c(f):
    return 5*((f-32)/9)
    

f = int(input("Enter temperature in farenheit: "))
c = convert_f_to_c(f)
print(round(c,2))

