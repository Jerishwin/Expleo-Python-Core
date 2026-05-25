string =input("Enter string: ")
digits =0
letters=0

for s in string:
    if s.isnumeric():
        digits+=1
    elif s.isalpha():
        letters+=1
    else:
        pass
print("Total digits: ",digits)
print("Total letters: ",letters)