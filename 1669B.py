t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = {}

    for x in a:
        count[x] = count.get(x, 0) + 1

        if count[x] == 3:
            print(x)
            break
    else:
        print(-1)