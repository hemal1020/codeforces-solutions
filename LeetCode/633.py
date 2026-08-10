import math
class Solution(object):
    def judgeSquareSum(self, c):
        a = int(math.sqrt(c))
        low = 0
        high = a
        while(low<=high):
            cal = low**2+high**2
            if(cal==c):
                return True
            elif(cal<c):
                low+=1
            else:
                high-=1
        return False        


sol = Solution()

print(sol.judgeSquareSum(73))   # Test case 1
print(sol.judgeSquareSum(2))   # Test case 2