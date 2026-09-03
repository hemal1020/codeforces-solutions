n =20
if(n==0 or n==1 or n==2):
    print(0) 
    exit()
a = [True]*n
f_count = 1

for i in range(2,int(n**0.5)+1) :
    if a[i]== False:
        continue
    j=i*2
    while(j<n) :
        if a[j]==True:
            a[j] = False
            f_count+=1  
        j+=i
print(n-f_count-1)
