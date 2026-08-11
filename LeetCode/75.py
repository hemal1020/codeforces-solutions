
class Solution:
    def sortColors(self, nums) :
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)
        
        # overwrite array in order
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0 + count1):
            nums[i] = 1
        for i in range(count0 + count1, len(nums)):
            nums[i] = 2


sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))









