
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if len({a[i] % 2 for i in range(0, n, 2)}) == 1 and \
       len({a[i] % 2 for i in range(1, n, 2)}) == 1:
        print("YES")
    else:
        print("NO")