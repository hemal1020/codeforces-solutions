
num = [2, 3, 5, 6, 2, 4, 5, 6, 6]
a = list(set(num))

h_idx = 0
h_num = 0
idx = 0
for i in a:
    if(h_num<num.count(i)):
 
        h_idx = idx
        h_num = num.count(i)
     
    idx+=1
idx-=1
print(a[h_idx])



