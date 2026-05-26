list1=[]

n=int(input("Enter the number of elements: "))

for i in range(0,n):
    elm = input("Enter the Element-{}:".format(i+1))
    list1.append(elm)

print(list1)

list2= input("Enter the Elements ith ,: ").split(',')
print(list2)

list3=list(map(int,input("Enter number usng space: ").split()))
print(list3)