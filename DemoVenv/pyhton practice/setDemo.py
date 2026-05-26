set1 = {4,3,2,1,2,3}
print(set1)
set1 = set([1,3,2,3,2])
print(set1)
set1 = {4,3,2,1,(2,3)}
print(set1)

set1.add(6)
print(set1)

set1.update([3,4,7],{8,1,2})
print(set1)

set1.discard(1)
set1.discard(1)
set1.remove(2)
print(set1)

print(set1.pop())
print(set1.pop())
print(set1)