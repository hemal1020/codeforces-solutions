import bisect
num = int(input())
list_ = list(map(int, input().split()))[:num]
s_day = sorted(list_)
for i in range(int(input())):
    inp = int(input())
    pos = bisect.bisect_right(s_day, inp)
    print(pos)
