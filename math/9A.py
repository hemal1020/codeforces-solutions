from math import gcd
def prob(n):
    rem = 6-n+1
    g = gcd(6,rem)
    print(f"{rem//g}/{6//g}")
    exit()
     
a,b= map(int,input().split())
if a>b:
    prob(a)
else:
    prob(b)    