t=(10)
t1=10,1,2,3
print(type(t1),type(t))
print(id(t1))
t1 = t1[1:]
print(id(t1))

addr='monty@python.com'
iname,domain=addr.split("@")
print(iname)
print(domain)
print(type(addr))
print(type(iname))

uto,rem=divmod(4,2)
print(uto)
print(rem)

