nums = [9,6,4,2,3,5,7,0,1]
l = len(nums)
print(((l*(l+1))//2)-sum(nums))


# Another method


missing = len(nums)

for i in range(len(nums)):
    missing ^= i ^ nums[i]

print(missing)