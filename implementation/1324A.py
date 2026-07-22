import sys
import bisect

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = [ai - bi for ai, bi in zip(a, b)]
d.sort()

ans = 0
for i in range(n):
    # find first index pos with d[pos] > -d[i]
    pos = bisect.bisect_right(d, -d[i])
    # we only count j > i, so valid j count is max(0, n - max(pos, i+1))
    if pos <= i:
        # some entries > -d[i] may start at i+1 or later
        pos = i + 1
    ans += n - pos

print(ans)
