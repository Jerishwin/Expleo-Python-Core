def sum(*num):
    odd_sum=0
    even_sum=0
    for i in num:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    print("Even Sum: ",even_sum)
    print("Odd Sum: ",odd_sum)

sum(1,2,3,4,5,6,7,8,9,10)