a, b = map(int, input().split())
c = 1
n = a
while (1):
    if n % 10 == 0 or n % 10 == b:
        print(c)
        exit()
    else:
        c += 1
        n += a
