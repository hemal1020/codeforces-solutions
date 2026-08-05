num = int(input())
for i in range(num):
    n = int(input())
    b = list(map(int, input().split()))
    print(max(b)*n) 
