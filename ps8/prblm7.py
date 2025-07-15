def remove_from_list(l,word):
    n = []
    for item in  l:
        if not(item== word):
            n.append(item.strip(word))
    return n


l = ["hungama", "YO", "Riya", "Hello", "YUP"]
n = input("Enter a word to remove: ")
print(remove_from_list(l,"an"))

