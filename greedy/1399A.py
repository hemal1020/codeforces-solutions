num = int(input())
for i in range(num):
    n = int(input())
    b = list(map(int, input().split()))[:n]
    st = sorted(b)
    f = 0
    if n > 1:
        for x in range(1, n):
            #print(st[x]-st[x-1])
            dif = st[x]-st[x-1]
            if dif > 1:
                f = 1
                break
        if f == 1:
            print("NO")
        else:
            print("YES")

    else:
        print("YES")
