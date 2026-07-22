x = input()
if x[0] == "-":
    if x[-1] < x[-2]:
        print("0") if x[:-2]+x[-1] == "-0" else print(x[:-2]+x[-1])
    elif x[-1] > x[-2] or x[-1] == x[-2]:
        print("0") if x[:-1] == "-0" else print(x[:-1])
else:
    print(x)
