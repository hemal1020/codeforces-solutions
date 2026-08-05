
num = [[1,3],[2,2]]
res = sorted(x for row in num for x in row)
le = len(res)
dup = None
sum = 0
n=0
s =0
for i in range(le):
    if(i<le-1):
        if (res[i] == res[i+1]):
            dup = res[i]
    n+=1        
    sum = sum + n
    s = s+ res[i]
print(sum,s)    
a = [dup, (sum-s)+dup]    
print(a)
