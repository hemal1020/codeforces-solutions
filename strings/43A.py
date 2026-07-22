n = int(input())
li = []
team1 = 0
team2 = 0
for i in range(n):
    temp = input()
    if n==1:
        print(temp)
        break
    elif temp not in li:
        if len(li) == 0:
            li.append(temp)
            team1 += 1
        elif temp != li[0]:
            li.append(temp)  
            team2 += 1  
    elif temp in li:                   
        if temp == li[0]:
            team1 += 1                    
        elif temp == li[1]:
            team2 += 1

if n>1:
    if team1 > team2:
        print(li[0])
    else:
        print(li[1])    

