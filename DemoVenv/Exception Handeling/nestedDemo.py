try:
    fh = open("Test.txt","w")
    try:
        fh.write("This is my test for exception handling")
    finally:
        print("Closeing the file")
        fh.close()
except IOError:
    print(IOError)
else:
    print("This is the else statement")
finally:
    print("Finnaly")