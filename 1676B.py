t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mn = min(a)
    print(sum(x - mn for x in a))