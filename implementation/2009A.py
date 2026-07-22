for i in range(int(input())):
    a,b = map(int,input().split())
    if a>=b:
        print("0")
        continue
    c = (a+b)//2
    print(c-a+b-c)
