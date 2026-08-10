class Solution(object):
    def maxProfit(self, nums):
        buy = 0
        sell = 0
        max_profit = 0
        i = 0
        j = 1
        while (j < len(nums)):
            profit = nums[j]-nums[i]          
            if (profit < 0):
                i = j
                j = j+1
                continue
            if (profit > max_profit):
                max_profit = profit
                buy = i
                sell = j  
            j += 1
        return max_profit


sol = Solution()
print(sol.maxProfit( [7,1,5,3,6,4]))   # Test case 2
print(sol.maxProfit([7,6,4,3,1]))   # Test case 2
