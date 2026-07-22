from math import gcd
import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    f = 0
    if n % 2 == 0:
        f = n
    else:
        f = n-1
    m = n//2
    print(gcd(f, m))


if __name__ == "__main__":
    t = int(input())   # number of test cases
    for _ in range(t):
        solve()
