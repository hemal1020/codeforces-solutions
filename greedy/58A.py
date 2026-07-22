import re
a = input()
if re.search(r"^\w*h\w*e\w*l\w*l\w*o\w*$", a):
    print("YES")
else:
    print("NO")
