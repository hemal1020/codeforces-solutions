a, b = map(int, input().split())
f=0
while(1):
    if a>b:
        print(f)
        break
    else:
        a*=3
        b*=2   
        f+=1 
