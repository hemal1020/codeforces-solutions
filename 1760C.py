t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = max(a)
    second = sorted(a)[-2]

    for x in a:
        if x == mx:
            print(x - second, end=" ")
        else:
            print(x - mx, end=" ")

    print()