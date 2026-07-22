import sys
input = sys.stdin.readline


def solve():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        if a <= b:
            print("Second")
        else:
            print("First")
    else:
        if b <= a:
            print("First")
            print("Second")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
