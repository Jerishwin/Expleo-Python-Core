import re
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'

text = "Contact us at Trainner@hotmail.com or gayatri.devi@mail.in"

res = re.findall(pattern,text)

print("{}".format(res))