a = list(map(int, input().split()))
largest = max(a)
for i in range(4):
    if largest-a[i] != 0:
        print(largest-a[i],end=" ")
