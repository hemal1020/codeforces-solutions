n = int(input())
res = 0
i = 3
count = 0
temp = 0
while (res <= n):
    count += 1
    if count == 1:
        res = 4
        temp = 3
    else:
        temp = temp+i
        res = res+temp
        i += 1
print(count)
