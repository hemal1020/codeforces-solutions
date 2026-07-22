list = []
num = int(input())
for i in input().split()[:num]:
    list.append(int(i))

even = 0
for i in range(3):
    if list[i] % 2 == 0:
        even += 1

if even >= 2:
    for i in range(num):
        if list[i] % 2 != 0:
            print(i+1)
else:
    for i in range(num):
        if list[i] % 2 == 0:
            print(i+1)
