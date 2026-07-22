li =[]
for i in input().split():
    li.append(int(i))
st = input()
sum =0
for y in st :
    sum+=li[int(y)-1]
print(sum)    

        