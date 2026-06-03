import re

text = "Alan Turing as a pioneer of theoretical computer science an ai. He as born on 23 june 1912 in London"
res=re.sub("theoretical","Practical",text)
print("Result = {}".format(res))