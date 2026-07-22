d = {}
z = int(input())
for i in range(z):
    temp = input()
    if temp not in d:
        d[temp] = 0
        print("OK")
    else:
        d[temp] += 1
        print(f"{temp}{d[temp]}")
