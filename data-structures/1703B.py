for i in range(int(input())):
    input()
    st = input()
    ct = ""
    res = 0
    for j in st:
        if j in ct:
            res += 1
        else:
            ct = ct+j
            res += 2
    print(res)
