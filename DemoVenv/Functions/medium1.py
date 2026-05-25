def sum(start,end):
    odd_sum=0
    even_sum=0
    for i in range(start,end+1):
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    print("Even Sum: ",even_sum)
    print("Odd Sum: ",odd_sum)
    print("difference beteen the sum: ",even_sum-odd_sum)

sum(1,1000)