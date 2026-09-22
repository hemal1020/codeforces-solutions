t = int(input())

for _ in range(t):
    points = [tuple(map(int, input().split())) for _ in range(4)]

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    side = max(max(x) - min(x), max(y) - min(y))

    print(side * side)