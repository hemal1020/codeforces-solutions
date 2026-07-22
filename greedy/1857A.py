for i in range(int(input())):
    n = int(input())
    odd=0
    for val in input().split()[:n]:
        if int(val)%2!=0:
            odd+=1
    if odd%2==0:    
        print("YES")   
    else:
        print("NO")         
