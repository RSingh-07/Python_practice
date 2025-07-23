with open("old.txt") as f:
    content1 = f.read()

with open("renamed_by_ python.txt","w") as f:
    f.write(content1)