x = int(input())
f=1
init = input()
for i in range(x-1):
    a = input()
    if init != a:
        init =a
        f+=1
print(f)



