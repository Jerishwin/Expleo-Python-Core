myobj = open("Test.txt",'w')
lines = ["One Batch\n","Two Batch\n","Penny and Dime\n"]
myobj.writelines(lines)

myobj.close()