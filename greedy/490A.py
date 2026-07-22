n = int(input())
one = []
two = []
thre = []
for i, val in enumerate(input().split()[:n]):
    if val == "1":
        one.append(i+1)
    if val == "2":
        two.append(i+1)
    if val == "3":
        thre.append(i+1)

m = min(len(one), len(two), len(thre))
print(m)
for i in range(m):
    print(one[i], two[i], thre[i])
