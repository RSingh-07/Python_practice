f = open("file.txt")

# lines = f.readlines()        f.readlines() reads all the lines from a file object f (opened using open()).
# print(lines, type(lines))     #    It returns a list, where each item is one line from the file, including the newline character \n.  


# line1 = f.readline()
# print(line1, type(line1))

line = f.readlines()
while(line != ""):
    print(line)
    line = f.readline()

f.close()