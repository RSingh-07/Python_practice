def myFunc():
    print("Hello World!")

myFunc()

# Is this file being run directly?
# or
# Is this file being imported from another file?
print(__name__) #__main__
# but in imported program it shows 'module'

if __name__ == "__main__":
    # If this code is directly executed by running the 
    # file its present in
    print("We are directly running this code")