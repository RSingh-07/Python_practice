#Lists contains any type of data

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])

# Lists are mutable 
friends[0] = "Grapes"
print(friends[0])

print(friends)

# BUT
# name = "Riya"

# print(name[0])
# name[0] = "S"   # TypeError: 'str' object does not support item assignment


print(friends[1:4])
print(friends[0][1])  #To access a character inside a list of strings, you use two levels of indexing

