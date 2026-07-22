def is_distinct(n):
    s = str(n)
    return len(set(s)) == len(s)


x = input()
y = int(x) + 1

while (1):
    if is_distinct(y):
        print(y)
        break
    else:
        y += 1
