input()
arr = list(map(int, input().split()))  # taking list of input
smallest = min(arr)  # find min value form list
maximum = max(arr)   # find max value from list

# Suppose array has smallest number more than once but we will take most right one
# [10,8,2,4,2,6] =[2,4] index of both 2 in the list
min_all_idx = [i for i, x in enumerate(arr) if x == smallest]
# [2,4]= 4  so most right small num in index 4
idx_min = min_all_idx[len(min_all_idx)-1]


idx_max = arr.index(maximum)  # most left max number

f = 0
if idx_max < idx_min:
    f = idx_max + len(arr)-(idx_min+1)
    print(f)
    exit()
f = idx_max + len(arr)-(idx_min+2)
print(f)
