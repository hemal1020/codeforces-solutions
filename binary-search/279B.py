n, t = map(int, input().split())
a = list(map(int, input().split()))

l = 0  # left pointer
curr_sum = 0
max_books = 0

for r in range(n):  # right pointer
    curr_sum += a[r]

    # shrink window while sum > t
    while curr_sum > t:
        curr_sum -= a[l]
        l += 1

    # update max length
    max_books = max(max_books, r - l + 1)

print(max_books)
