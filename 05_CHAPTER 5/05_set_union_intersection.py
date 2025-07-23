s1 = {1, 45, 6}
s2 ={7, 8, 1, 78}

#Combines all elements from both sets (removes duplicates). |
print(s1.union(s2))

#Returns only the common elements. &
print(s1.intersection(s2))

#Returns elements in A but not in B.  -
print(s1.difference(s2))

# Returns elements that are in A or B but not in both.  ^
print(s1.symmetric_difference(s2))


# Returns True if A is a subset of B.  <=
print(s2.issubset(s1))

