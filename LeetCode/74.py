class Solution(object):

    def binary_search(self, matrix, m, target):
        left = 0
        right = len(matrix[m]) - 1
        arr = matrix[m]

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1

    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            lt = len(matrix[mid])

            if matrix[mid][0] <= target and matrix[mid][lt - 1] >= target:
                r = self.binary_search(matrix, mid, target)

                if r != -1:
                    return True
                else:
                    return False

            elif matrix[mid][0] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False