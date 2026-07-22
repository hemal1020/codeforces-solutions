for i in range(int(input())):
    temp = int(input())
    if (temp//2) % 2 == 0:
        print('YES')
        arr = []
        even = 0
        tot = 0
        tt = 0
        idx = 0
        odd = 1
        for y in range(temp//2):
            even = even+2
            arr.insert(idx, even)
            tot += even
            arr.append(odd)
            tt += odd
            odd = odd+2
            idx += 1  
        arr[temp-1] = arr[temp-1]+tot-tt
        print(*arr)
    else:
        print("NO")    
