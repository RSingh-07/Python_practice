print("Hey Riya!!")

name = "Riya"
length = len(name)
print(length)

nameshort = name[0:2] # start from index 0 all the way till 2 (excluding 2)
print(nameshort)
char1 = name[-1]
print(char1)


#negative indexing
name2 = "Harry"
print(name2[-4:-1])
print(name2[1:4])


print(name2[:4]) # is same as [0:4]
print(name2[1:]) # is same as [1:5]


#skip value
word = "amazing"

print(word[1: 6: 2])

