l = [3, 53, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index +=1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")


# What enumerate(l) does:
# It converts your list into:

# [(0, 3), (1, 53), (2, 53), (3, 535)]

# So on each loop, it gives:
# index: the position (0, 1, 2, ...)
# item: the value at that index

# (automatic index tracking, cleaner, shorter, more readable)
# we can also start from custom index
# for index, item in enumerate(l, start=1):
    # print(f"{index}. {item}")