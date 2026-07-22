x = input()
i = 1
f = 1
temp = x[0]
while (i < len(x)):
    if temp == x[i]:
        f += 1
        if f == 7:
            print("YES")
            exit()
    else:
        temp = x[i]
        f = 1
    i += 1

print("NO")
