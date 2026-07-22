num = int(input())
one = 0
two = 0
three = 0
final = 0
b = list(map(int, input().split()))
for i in range(num):
    temp = b[i]
    if temp == 4:
        final += 1
    elif temp == 2 and two > 0:
        two -= 1
        final += 1
    elif temp == 2 and two == 0:
        two += 1
    elif temp == 3 and one > 0:
        one -= 1
        final += 1
    elif temp == 3 and one == 0:
        three += 1
    elif temp == 1 and three > 0:
        three -= 1
        final += 1
    elif temp == 1 and three == 0:
        one += 1
final = final + one//4
one = one % 4

if (one+two) == 0:
    pass
elif (one+two) <= 4:
    final = final + 1
else:
    final = final + 2

print(final+three)
