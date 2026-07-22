a, b = map(int, input().split())
c = 240-b
problem = 0
i=1
n=0
while (1):    
    problem = problem + 5*i
    if problem <= c:
        n+=1     
        if n==a:
            print(n)
            exit()
    else:
        break
    i+=1
print(n)
