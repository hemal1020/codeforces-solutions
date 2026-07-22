# 🔹 Example with bisect
import bisect

arr = [1, 3, 4, 7, 9, 11]

# Find position to insert 5
pos = bisect.bisect(arr, 6)
print(pos)  # Output: 3


# ➡️ Here, 5 should be inserted at index 3 (between 4 and 7).

# 📌 Main Functions in bisect

# bisect_left(arr, x)
# Returns the index where x should be inserted to keep order, placing it before any existing equal elements.




arr = [1, 3, 3, 3, 7]
print(bisect.bisect_left(arr, 3))  # Output: 1
# bisect_right(arr, x) or bisect(arr, x)
# Returns the index where x should be inserted, placing it after any existing equal elements.
print(bisect.bisect_right(arr, 3))  # Output: 4




# insort_left(arr, x)
# Inserts x into arr at the index given by bisect_left (before existing duplicates).
bisect.insort_left(arr, 3)
print(arr)  # [1, 3, 3, 3, 3, 7]


# insort_right(arr, x) or insort(arr, x)
# Inserts x into arr at the index given by bisect_right (after existing duplicates).

arr = [1, 3, 3, 3, 7]
bisect.insort_right(arr, 3)
print(arr)  # [1, 3, 3, 3, 3, 7]


# 🔹 1. Check if an element exists (like binary search)

arr = [1, 3, 4, 7, 9, 11]
x = 7

pos = bisect.bisect_left(arr, x)
if pos < len(arr) and arr[pos] == x:
    print("Found at index:", pos)
else:
    print("Not found")
