list=[]
for i in input().split():
    list.append(i)
buy = len(list)-len(set(list))
print(buy)