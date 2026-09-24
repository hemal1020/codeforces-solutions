t = int(input())

for _ in range(t):
    x, y, n = map(int, input().split())
    
    ans = n - (n - y) % x
    
    if ans < y:
        ans += x
    
    print(ans)