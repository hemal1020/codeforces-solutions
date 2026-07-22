a = int(input())
li = []
cur = 0
mx = 0
for i in range(a):
    temp = input()
    if temp[0] == "+":
        li.append(temp[2:])
        cur += 1
        if cur > mx:
            mx += 1
    if temp[0] == "-":
        if temp[2:] in li:
            li.remove(temp[2:])      
            cur -= 1
        else:
            mx += 1
        
print(mx)
