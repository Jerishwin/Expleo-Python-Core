import re

text = "Alan Turing as a pioneer of theoretical computer science an ai. He as born on 23 june 1912 in London"
res=re.search("^Alan.*London$",text)
print(res)
if(res):
    print("We have a match")
else:
    print("We don't have a match")

res=re.search("Turing",text)
print("Result = {} and start,end position = {}".format(res,res.span()))