class Solution(object):
    def twoSum(self, nums, target):
        n ={}
        for i in range(len(nums)):
            first = nums[i]
            second = target - first
            if second in n:
                return n[second],i
            n[nums[i]]=i


sol = Solution()
print(sol.twoSum([0,2,9,8,5,3,15,78,7,4],5))