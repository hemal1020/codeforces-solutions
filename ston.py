x = int(input())
y = input()

r = 0
for i in range(1, x):
    if y[i] == y[i-1]:
        r += 1

print(r)
