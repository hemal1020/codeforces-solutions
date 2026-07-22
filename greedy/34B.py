a, b = map(int, input().split())
li = [int(i) for i in input().split()[:a]]
result = 0
for i in range(b):
    m = min(li)
    if m < 0:
        li.remove(m)
        result += m
print(abs(result))
