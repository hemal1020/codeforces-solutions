t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    S = sum(a)
    print(-S + 2 * max(a))
