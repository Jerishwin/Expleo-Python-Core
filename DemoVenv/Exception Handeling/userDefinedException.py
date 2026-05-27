class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass


num=10

while True:
    try:
        a=int(input("Enter a number: "))

        if a>num:
            raise ValueTooLargeError
        elif a<num:
            raise ValueTooSmallError
        break
    except ValueTooSmallError:
        print("This is small try again")
    except ValueTooLargeError:
        print("this is large try again")

print("you guessed it")