for i in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        x = (23-x)*60
        y = 60-y
    elif x > 0 and y == 0:
        x = (24-x)*60
    elif x==0 and y>0:
        x = 23*60 
        y = 60-y   
    print(x+y)
    


