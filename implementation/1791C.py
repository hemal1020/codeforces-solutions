import sys
input = sys.stdin.readline


def solve():
    x = int(input())
    str = input()[:x]
    count = 0
    j = x
    for i in range(x//2):
        if str[i] == "0" and str[x-1] == "1":
            count += 2
            x -= 1
        elif str[i] == "1" and str[x-1] == "0":
            count += 2
            x -= 1
        else:
            break
    print(j-count)


if __name__ == "__main__":
    t = int(input())   # number of test cases
    for _ in range(t):
        solve()
