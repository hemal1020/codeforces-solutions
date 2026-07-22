mi = 0
cr = 0
for i in range(int(input())):
    m, c = map(int, input().split())
    if m > c:
        mi += 1
    elif c > m:
        cr += 1
if mi > cr:
    print("Mishka")
elif cr > mi:
    print("Chris")
else:
    print("Friendship is magic!^^")
