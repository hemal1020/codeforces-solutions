t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_a = min(a)
    min_b = min(b)

    ans = 0

    for i in range(n):
        x = a[i] - min_a
        y = b[i] - min_b

        ans += min(x, y)
        ans += abs(x - y)

    print(ans)