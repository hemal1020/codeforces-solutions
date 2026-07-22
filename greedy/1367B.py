import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    idx = 0
    even = 0
    odd = 0
    for i in input().split()[:n]:
        temp = int(i)
        if idx % 2 == 0 and temp % 2 == 0:
            pass
        elif idx % 2 == 0 and temp % 2 != 0:
            even += 1
        elif idx % 2 != 0 and temp % 2 != 0:
            pass
        elif idx % 2 != 0 and temp % 2 == 0:
            odd += 1
        idx += 1
    if even == odd:
        print(even)
    else:
        print(-1)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
