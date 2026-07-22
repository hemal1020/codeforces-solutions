n, h = map(int, input().split())
heights = list(map(int, input().split()))

w = 0
for height in heights:
    if height > h:
        w += 2
    else:
        w += 1

print(w)
