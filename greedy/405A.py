list=[]
num = int(input())
for i in input().split()[:num]:
    list.append(int(i))

for x in sorted(list):
    print(x,end=" ")    