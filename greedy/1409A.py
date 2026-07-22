num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    c = abs(a-b)
    count = 0
    while (1):
        if c >= 10:
            n = len(str(c)) - 1
            count += (c//pow(10, n))*pow(10, n-1)
            c = c % pow(10, n)
        elif c > 0 and c < 10:
            count += 1
            break
        else:
            break
    print(count)
