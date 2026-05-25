n=int(input("Enter a number: "))
i=1
sum=0
while i<=n:
    num = int(input("Enter user inputs:"))
    if num==1:
        break
    else:
        sum=sum+num
    i=i+1
print(sum)
