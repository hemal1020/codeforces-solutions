p, n = map(int, input().split())
drag = []
bon = []
for i in range(n):
    d, b = map(int, input().split())
    drag.append(d)
    bon.append(b)

pairs = sorted(zip(drag, bon))
d, b = zip(*pairs)
for i in range(len(d)):
    if p > d[i]:
        p += b[i]
    else:
        print("NO")
        exit()
print('YES')
