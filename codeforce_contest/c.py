import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(set(a))

    best = 1
    cur = 1
    for i in range(1, len(b)):
        if b[i] == b[i-1] + 1:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)

    res.append(str(best))

print('\n'.join(res))
