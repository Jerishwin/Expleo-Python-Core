try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=a/b
except (Exception):
    print(Exception)
else:
    print(c)
finally:
    print("executed")