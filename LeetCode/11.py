class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        max_area = 0
        while (l < r):
            area = (r-l)*min(height[r], height[l])
            if area > max_area:
                max_area = area
            if height[r]<height[l]:
                r-=1
            else:
                l+=1   
        return max_area             


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
