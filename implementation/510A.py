a, b = map(int, input().split())
f = 0
for i in range(a):
    if (i+1) % 2 == 0 and f == 0:
        print("."*(b-1)+"#")
        f = 1
    elif (i+1) % 2 == 0 and f == 1:
        print("#"+"."*(b-1))
        f = 0
    else:
        print("#"*b)
