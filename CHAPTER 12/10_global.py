a = 89
def fun():
    # ‘global’ keyword is used to modify the variable outside of the current scope.
    global a
    a = 3
    print(a)


fun()
print(a)