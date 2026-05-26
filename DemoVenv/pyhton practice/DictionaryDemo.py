dict1 = {}
dict1 = {1:"apple",2:'Banana'}
dict1 = {1:'CSE','name':'Ram','list':[123],'tupel':(10,11)}
print(type(dict1[1]))
print(type(dict1['name']))
print(type(dict1['list']))
print(type(dict1['tupel']))

dict2 =dict(x=5,y=0)
print(dict2)
dict2 =dict({'x':5,'y':0})
print(dict2)
dict2 =dict([('x',5),('y',0)])
print(dict2)

fam={
    'child1':'gojo','child2':'satoru'
}

print(fam['child2'])

fam['child3']='kavin'
print(fam)

for x in fam:
    print(x,fam[x])

print(fam.popitem())
print(fam)

f1={'child2':'lavanya gopal'}
fam.update(f1)
print(fam)
suare={x:x*x for x in range(20) if x*x%2==0}
print(suare)