class Solution(object):
    def peakIndexInMountainArray(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid]>nums[mid-1] and nums[mid]> nums[mid+1]:
                return mid

            elif nums[mid] > nums[mid-1]:
                # Target is in the right half
                left = mid + 1

            else:
                # Target is in the left half
                right = mid - 1

        return -1

sol = Solution()
print(sol.peakIndexInMountainArray([0,2,1,0]))    