t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    s = input()
    target = input()

    count = 0

    while target not in s and len(s) < m:
        s += s
        count += 1

    if target in s:
        print(count)
    else:
        s += s
        count += 1

        if target in s:
            print(count)
        else:
            print(-1)