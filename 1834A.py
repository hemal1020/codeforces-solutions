t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    neg = a.count(-1)

    if neg % 2 == 1:
        print(1)
    else:
        print(0)