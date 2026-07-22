a = int(input())
for i in range(a):
    li = [input() for x in range(int(input()))]
    c = 0
    pat = ""
    idx = 0
    for j in range(len(li)):
        if "1" in li[j]:
            c = li[j].count("1")
            pat = li[j]
            idx = j
            break
    f = 0
    cnt = 0
    for y in range(len(li)):
        if idx == y:
            pass
        elif pat == li[y]:
            cnt += 1
            if cnt == c:
                f = 1
                break
        else:
            cnt = 0
    if f == 1:
        print("SQUARE")
    else:
        print("TRIANGLE")
