list = []
a, b = map(int, input().split())
for i in input().split()[:b]:
    list.append(int(i))

li = sorted(list, reverse=True)
low = li[0]-li[a-1]
for i in range(1,b-a+1):
    if li[i]-li[i+a-1] < low:
        low = li[i]-li[i+a-1]
print(low)
