myobj = open("testing.txt",'w')
a=input("Enter String: ")
myobj.write(a)
myobj.close()
myobj = open("testing.txt",'r')
b=myobj.read()
print(b)

myobj.close()