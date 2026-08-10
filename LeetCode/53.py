class Solution(object):
    def maxSubArray(self, nums):
        c_max = 0
        h_max = float('-inf')
        for i in range(len(nums)):
            c_max = c_max + nums[i]
            h_max= max(c_max, h_max)
            if(c_max<0):
                c_max=0
        return h_max        


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))   # Test case 2
print(sol.maxSubArray([1]))   # Test case 2