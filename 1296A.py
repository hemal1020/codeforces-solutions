t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)

    if s % 2 == 1:
        print("YES")
    elif any(x % 2 == 1 for x in a) and any(x % 2 == 0 for x in a):
        print("YES")
    else:
        print("NO")