num = int(input())
min=0
max=0
f=0
c=0
for x in input().split()[:num]:
    i = int(x)
    if c==0:
        min=i
        max =i
    else:
        if i>max:
            f+=1
            max =i
        if i<min:
            f+=1
            min=i    
    c+=1        
print(f)    
