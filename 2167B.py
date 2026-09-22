t = int(input())

for _ in range(t):
    n = int(input())

    s, target = input().split()

    if sorted(s) == sorted(target):
        print("YES")
    else:
        print("NO")