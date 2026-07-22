import sys
input = sys.stdin.readline


def solve():
    # Example: read n and a list
    n = int(input())
    arr = list(map(int, input().split()))

    # Example logic (replace with your solution)
    ans = sum(arr)
    print(ans)


if __name__ == "__main__":
    t = int(input())   # number of test cases
    for _ in range(t):
        solve()
