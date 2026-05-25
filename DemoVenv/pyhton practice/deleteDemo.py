greet="welcome"

str1="hello, "
str2="world!"

print(greet)

print(greet[-1])
print(len(greet))

for i in greet:
    print(i)

print(greet[::-1])
print(greet[-7:-1])

str3=str1+str2
print(str3)
print(str1*3)

print(str3.upper())
print(str3.lower())
print(str3.find('o'))
print(str3.replace("world","EARTH"))

print("J"+str3[-6:-1])


if "co" in greet:
    print("Yes")
del greet

print(greet)