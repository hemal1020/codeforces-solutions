a=[]
b=[]
len = int(input())
for i in range(len):
    temp = input().split(" ")
    a.append(temp[0])
    b.append(temp[1])
f=0
for i in range(len):
    for y in range(len):
        if a[i]==b[y]:
            f+=1
print(f)
