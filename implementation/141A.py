a=input()
b= input()
c= input()
d=a+b
if len(c)==len(d):
    for i in range(len(d)):
        if d[i] in c:
            c = c.replace(d[i], "", 1)
    if len(c)==0:
        print("YES") 
        exit()
print("NO")              

