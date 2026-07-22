list = []
n = int(input())
for i in input().split()[:n]:
    list.append(int(i))
f = 1
ff = 1
for i in range(1, len(list)):
    if list[i] > list[i-1] or list[i] == list[i-1]:
        f += 1
        if f > ff:
            ff = f
    else:
        f = 1
print(ff)
