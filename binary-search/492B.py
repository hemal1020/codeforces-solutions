list = []
n, street_length = map(int, input().split())
for i in input().split()[:n]:
    list.append(int(i))

s_arr = sorted(list)
max_ = 0
for i in range(1, n):
    temp = s_arr[i]-s_arr[i-1]
    if temp > max_:
        max_ = temp
max_ = max_/2
semi = max(max_, street_length-s_arr[n-1], s_arr[0])
print(semi)
