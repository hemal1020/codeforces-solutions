list=[]
per =0
num = int(input())
for i in input().split()[:num]:
   per = per+int(i)/num
print(f"{per:.12f}")   
