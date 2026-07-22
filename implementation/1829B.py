for i in range(int(input())):
    num = int(input())
    result = 0
    zero = 0
    for y in input().split()[:num]:
        if y == "0":
            zero += 1
        elif y == "1":
            zero = 0
        if zero > result:
            result = zero
    print(result)        
