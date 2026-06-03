import re
text = "Alan Turing as a pioneer of theoretical computer science an ai. He as born on 23 june 1912 in London"

res = re.search("computer",text)
print("Match obj = {}".format(res))
print("_"*30)

print("Group =",res.group())
print("_"*30)

print("Start =",res.start())
print("_"*30)

print("End =",res.end())
print("_"*30)

print("Span =",res.span())
print("_"*30)

print("re =",res.re)
print("_"*30)

print("String =",res.string)
print("_"*30)

text=r'Search \\ in string'
res = re.search(r"\\",text)

print("r =",res)
print("_"*30)