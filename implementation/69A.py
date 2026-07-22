num = int(input())
xs = 0
ys = 0
zs = 0
for i in range(num):
    x, y, z = map(int, input().split())
    xs += x
    ys += y
    zs += z

if xs == 0 and ys == 0 and zs == 0:
    print('YES')
else:
    print("NO")
