def output(a):
    key = {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five',
       '6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero'}
    string=''
    for i in a:
        string +=key[i]+" "
    return string

a=input("Enter a number: ")

print(output(a))