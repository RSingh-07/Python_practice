f = open("poems.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content ")
else:
    print("The word twinkle is not in the content ")
f.close()

