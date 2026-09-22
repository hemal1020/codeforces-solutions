t = int(input())

for _ in range(t):
    time = input()
    h, m = map(int, time.split(':'))

    if h == 0:
        h = 12
        period = "AM"
    elif h < 12:
        period = "AM"
    elif h == 12:
        period = "PM"
    else:
        h -= 12
        period = "PM"

    print(f"{h:02d}:{m:02d} {period}")