import traceback

try:
    num=int(input("Enter a positive number: "))
    if(num<0):
        raise ValueError("This is a negative number")
except ValueError as a:
    traceback.print_exc()
print("Sucess")