t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()

    ans = 0

    for ch in "ABCDEFG":
        count = s.count(ch)
        if count < m:
            ans += m - count

    print(ans)