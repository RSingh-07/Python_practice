def main():
    try:
        a = int(input("Enter a number: ")) #if exception not handled the prgm crashes here none of the further lines will be executed
        print(a)
        return
        
    except Exception as e:
        print(e)
        return 

    # Finally guarantees execution
    finally:
        print("Hey I am inside of finally")


main()

# If an exception occurs and is not handled, or if you use return or exit() in your code, the line after try-except may not be reached.

# But finally will always run, even in those situations.

# When working with files, network connections, or databases, finally is essential(f.close())
