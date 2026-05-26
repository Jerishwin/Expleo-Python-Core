str1 = input("Enter a String: ")
list1 = str1.split()

for i in list1:
    if any(ch.isdigit() for ch in i):
        print(i)