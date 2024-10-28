from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length - 1

        while (left < right):
            mid = (right + left) // 2

            if (nums[mid] > nums[mid+1]):
                right = mid
            else:
                left = mid + 1

        return left
            