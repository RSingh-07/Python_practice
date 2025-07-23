list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, item in enumerate(list, start=1):
    if index in[3, 5, 7]:
        print(f"The element at position {index} is {item}")

