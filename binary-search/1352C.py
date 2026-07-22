for i in range(int(input())):
    a, b = map(int, input().split())
    temp = 0
    mod = 0
    res = b
    if b >= a:
        while (b >= a):
            temp = b//a
            res = res+temp
            mod = b % a
            b = temp+mod
        res = res
        print(res)
    else:
        print(b)
