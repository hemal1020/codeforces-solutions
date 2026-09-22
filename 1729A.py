t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    time1 = a - 1
    time2 = abs(b - c) + c - 1

    if time1 < time2:
        print(1)
    elif time2 < time1:
        print(2)
    else:
        print(3)