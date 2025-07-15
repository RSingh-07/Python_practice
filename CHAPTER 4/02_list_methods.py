friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)

friends.append("Harry") # add element at last 
print(friends)

l1 = [1, 34, 62, 2, 6, 11]

l1.sort() # changes original list
print(sorted(l1)) # doesnt chnage original list, creates new list
#print(l1.reverse())

# l1.insert(7, 72) # insert at specified position

# print value 
#print(l1.pop(3))
l1.pop(3)
print (l1)


l1.remove(62)
print(l1)

print(friends == l1)