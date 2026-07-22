import sys
input = sys.stdin.readline


def solve():
    n = input().strip()
    le = len(n)
    b = (int(n[0])-1)*10
    if le == 1:
        b += 1
    elif le == 2:
        b += 3
    elif le == 3:
        b += 6
    elif le == 4:
        b += 10
    print(b)


if __name__ == "__main__":
    t = int(input())   # number of test cases
    for _ in range(t):
        solve()
