list=[]
num = int(input())
for i in input().split()[:num]:
    list.append(int(i))

for val in sorted(enumerate(list), key=lambda x: x[1]):
    print(val[0]+1,end=" ")

   