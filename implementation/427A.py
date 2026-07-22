list = []
num = int(input())
oc = 0
police = 0
for i in input().split()[:num]:
    if i == "-1" and police == 0:
        oc += 1
    elif i == "-1" and police > 0:
        police -= 1
    else:
        police += int(i)

print(oc)