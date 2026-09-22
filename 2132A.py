t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    m = int(input())
    c = input()
    p = input()

    for i in range(m):
        if p[i] == 'D':
            s = s + c[i]
        else:
            s = c[i] + s

    print(s)