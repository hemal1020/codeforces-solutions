a, b = map(int, input().split())
f=0
g=0
while(1):
    if a>0 and b>0:
        a-=1
        b-=1
        f+=1
    elif a>1 and b==0:
        a-=2
        g+=1
    elif a==0 and b>1:
        b-=2   
        g+=1
    else:
        break      
print(f,g)