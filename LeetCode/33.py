class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target is inside the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # Search in the right half
                    left = mid + 1

            # Right half is sorted
            else:

                # Target is inside the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # Search in the left half
                    right = mid - 1

        return -1