import sys
import math
from collections import Counter, defaultdict, deque

# Fast I/O
input = sys.stdin.readline

# Output buffering (collect all answers and print once at the end)
output = []


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Example logic (replace with problem solution)
    ans = sum(arr)
    output.append(str(ans))


if __name__ == "__main__":
    t = int(input())   # number of test cases
    for _ in range(t):
        solve()

    # Print all results at once
    sys.stdout.write("\n".join(output))
