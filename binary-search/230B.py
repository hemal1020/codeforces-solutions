list = []
num = int(input())
for i in input().split()[:num]:
    list.append(int(i))

for i in range(num):
    x = 1
    f = 0
    
    while (1):
        if list[i] % x == 0:
            f += 1
        if f == 3 and x == list[i]:
            print('YES')
            break
        if f < 3 and x == list[i]:
            print("NO")
            break
        if f > 3:
            print("NO")
            break
        x += 1
