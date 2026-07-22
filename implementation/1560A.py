for i in range(int(input())):
    a = int(input())
    i=0
    num=0
    while i<a:
        num+=1
        if num%3==0 or "3" in str(num)[-1]:
            pass
        else:        
            i+=1
    print(num)    