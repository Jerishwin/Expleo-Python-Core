str1=input("Enter String: ")
out=""
for i in range(len(str1)):
    if str1[i].isalpha() or str1[i].isdigit() or str1[i].isspace():
        out+=str1[i]
    else:
        out+='#'

print(out)