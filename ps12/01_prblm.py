# try:
#     with(
#         open("file1.txt") as f1,
#         open("file2.txt") as f2,
#         open("file3.txt") as f3
#     ):
#         pass
# except FileNotFoundError as e:
#   print(f"{e.filename} is missing.")
# print("Thankyou!")

# doesnt check other files

files = ["file1.txt", "file2.txt", "file3.txt"]

for filename in files:
    try:
        with open(filename) as f:
            print(f"{filename} opened successfully")
    except FileNotFoundError:
        print(f"{filename} is missing.")