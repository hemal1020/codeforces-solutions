for i in range(int(input())):
    num = int(input())
    ml = 1
    sm = 0
    flag = 1
    for j in input().split()[:num]:
        temp = int(j)
        if flag == 1:
            sm = temp
            flag = 2
            continue
        if temp < sm:
            ml = ml*sm
            sm = temp
        else:
            ml = ml*temp
    ml = (ml)*(sm+1)
    print(ml)
