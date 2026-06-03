import re

text = "Alan Turing as a pioneer of theoretical computer science an ai. He as born on 23 june 1912 in London"

res = re.findall("\AAlan",text)
print("Result for \A = ",res)
print("_"*100)

res = re.findall(r"\bLon",text)
print("Result for \\b = ",res)
print("_"*100)

res = re.findall("[^a-zA-Z]",text)
print("Result for [^a-zA-Z] = ",res)
print("_"*100)

res = re.findall("\d",text)
print("Result for \d = ",res)
print("_"*100)

res = re.findall("\D",text)
print("Result for \D = ",res)
print("_"*100)

res = re.findall("\s",text)
print("Result for \s = ",res)
print("_"*100)

res = re.findall("\S",text)
print("Result for \S = ",res)
print("_"*100)

res = re.findall("\w",text)
print("Result for \w = ",res)
print("_"*100)

res = re.findall("\W",text)
print("Result for \W = ",res)
print("_"*100)

res = re.findall("London\Z",text)
print("Result for \Z = ",res)
print("_"*100)