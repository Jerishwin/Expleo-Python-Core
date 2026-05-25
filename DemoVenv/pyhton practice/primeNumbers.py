l = int(input("Enter lower Limit: "))
u = int(input("Enter upper Limit: "))
for num in range(l,u+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)    
