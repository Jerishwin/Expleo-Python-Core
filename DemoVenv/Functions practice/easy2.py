def prime(num):
    if num<2:
        return
    for i in range(2,num-1):
        if num%i==0:
            return
    print(num)


for i in range(1,101):
    prime(i)