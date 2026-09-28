t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if n == a == b:
        print("Yes")
    elif a + b + 2 <= n:
        print("Yes")
    else:
        print("No")