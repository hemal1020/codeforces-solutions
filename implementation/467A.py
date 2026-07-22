a = int(input())
f=0
for i in range(a):
    a,b = map(int,input().split())
    if b-a>=2:
        f+=1
print(f)    