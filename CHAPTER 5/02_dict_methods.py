marks ={
    "Riya": 99,
    "Shriya" : 56,
    "Rohan": 23
}

# print(marks.items()) #list of tuples 
# print(marks.keys())
# print(marks.values())

# marks.update({"Riya":100})  #mutable
# print(marks)

print(marks.get("Harry")) # Prints None
# print(marks.get("Riya"))
# print(marks["Harry2"])  # Returns KeyError

print(marks.popitem()) #removes last item added