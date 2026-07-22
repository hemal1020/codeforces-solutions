s = input().strip()
if s == "{}":
    result = []
else:
    result = s.strip("{}").split(", ")


print(len(set(result)))
