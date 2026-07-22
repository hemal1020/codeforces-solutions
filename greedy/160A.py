list=[]
sum=0
num = int(input())
for i in input().split()[:num]:
   list.append(int(i))
   sum = sum+int(i)
my=0
f=1
sl=[]
for n in sorted(list,reverse=True):
   sl.append(n)
for i in range(num):
   my = my+sl[i]
   if my>sum-my:
      break
   f+=1
print(f)   
