ele=[x**2 for x in range(10) if x**2%2==0]
print(ele)

def increment(list2):
    list2=[1,2,3,4,5]
    for i in range(0,len(list2)):
        list2[i]+=5
    print(id(list2))

list1=[10,20,30,40]
print(list1)
increment(list1)
print(list1)
print(id(list1))