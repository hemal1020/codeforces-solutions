"""
****time complexity O(n log k)****
better than sorting algorithm which is O(n lon n)
"""

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = [] # black heam memeor
        for i in nums:
            heapq.heappush(heap, i)
            if (len(heap)>k):
                heapq.heappop(heap)

        return heap[0]        




sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4],2))         