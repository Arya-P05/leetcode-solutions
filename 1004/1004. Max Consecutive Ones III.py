from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ones = 0
        temp_k = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                temp_k += 1
            
            while temp_k > k:
                if nums[left] == 0:
                    temp_k -= 1
                left += 1
            
            max_ones = max(max_ones, right - left + 1)

        return max_ones