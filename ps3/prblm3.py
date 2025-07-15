name = "Harry is a  good boy and"

print(name.find("  ")) # -1 if not found
print(name.index("  ")) # ValueError if not found

print(name.replace("  ", " ")) # replace double space from prblm 3 with single space
print(name) # Strings are immutable which means that you cannot change them by running functions on them

