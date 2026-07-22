n = int(input())

parts = []
for i in range(1, n+1):
    if i % 2 == 1:
        parts.append("I hate")
    else:
        parts.append("I love")

print(" that ".join(parts) + " it")
