
def demo(num1,num2,num3=4):
    add = num1+num2+num3
    return add

print(demo(1,2))
#----------------------------
def key(name,msg):
    print("Hello, ",name,msg)

key(msg="Message",name="John")
key(1.3,2.4)
#------------------------------
def emp(*name):
    for emp in name:
        print("Hello, ",emp)

emp("Rachel","John","Albert","Laden")
#--------------------------------

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))