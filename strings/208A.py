import re
s = input()
a = re.sub(r"(WUB)+", " ", s)
print(a.lstrip())
