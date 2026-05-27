myobj = open("Test.txt",'w')
a = myobj.write("Hey i have started using files in Python\n")
print(a)
b=54
a=myobj.write(str(b))
print(a)
myobj.close()