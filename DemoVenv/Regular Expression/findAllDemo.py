import re
text = "Alan Turing as a pioneer of Turing theoretical computer science an ai. He asTuringasdasda born on 23 june 1912 in London"

res=re.findall('Turing',text)

print("Result = {}".format(res))