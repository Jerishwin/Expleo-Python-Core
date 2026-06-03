import re
pattern = r'\b\w+ing\b'

text = "Walking and talking are important activities."

res = re.findall(pattern,text)

print("{}".format(res))