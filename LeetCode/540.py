class Solution(object):
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even so we can compare it with the next element
            if mid % 2 == 1:
                mid -= 1

            # Pair is correct, so single element is on the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2

            # Pair is broken, so single element is on the left
            else:
                right = mid

        return nums[left]

sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))            