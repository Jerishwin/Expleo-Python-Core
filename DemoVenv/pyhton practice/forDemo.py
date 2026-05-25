n = int(input("Enter a digit: "))
if n == 1:
    fac = 1
elif n>0:
    fac =1
    for i in range(2,n+1):
        fac = fac*i
else:
    print("error")

print(fac)
