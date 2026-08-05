import bisect as bs
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = nums1[:m]
        for i in range(n):
            bs.insort_left(temp, nums2[i])
        nums1[:]= temp
