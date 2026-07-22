x = int(input())
mx = 0
ma = 0
mb = 0
for i in range(x):
    a, b = map(int, input().split())
    ma += a
    mb += b
    if mx < mb-ma:
        mx = mb-ma

print(mx)
