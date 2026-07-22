a = input()
b = input()
if len(a) != len(b):
    print("NO")
    exit()

l = len(a)
for i in range(l):
    if a[i] != b[l-1]:
        print("NO")
        exit()
    l -= 1
print("YES")
