t = int(input())

for _ in range(t):
    s = input()

    smallest = s[0]

    for digit in s:
        if digit < smallest:
            smallest = digit

    print(smallest)