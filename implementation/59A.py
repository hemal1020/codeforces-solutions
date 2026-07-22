import re
x = input()
uname = re.sub(r"[a-z]+", "", x)  # replace with
if len(uname) > len(x)-len(uname):
    print(x.upper())
else:
    print(x.lower())

# another method
[print(x.upper()) if len(uname) > len(x)-len(uname) else print(x.lower())]
