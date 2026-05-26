t=list()
print(type(t))

string ="Hello"
t=list(string)

print(t)

del t[3]
print(t)

for i in t:
    print(i)
print()
for i in range(len(t)):
    print(t[i])

print(t*3)