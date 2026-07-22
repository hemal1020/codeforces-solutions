t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if a.count(k) >= 1:
        print("YES")
    else:
        print("NO")
