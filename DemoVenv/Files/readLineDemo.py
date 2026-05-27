myobj = open("Test.txt",'r')
a = myobj.readlines()
for line in a:
    ords = line.split()
    print(ords)

d=a.splitlines()
print(d)