k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
damage =0
for i in range(d):
    temp = i+1
    if temp%k==0 or temp%l==0 or temp%m==0 or temp%n==0 :
        damage+=1

print(damage)
