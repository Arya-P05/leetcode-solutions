from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_zeros = 0
        left_idx = 0
        num_zeros = 0

        for right_idx in range(len(nums)):
            if nums[right_idx] == 0:
                num_zeros += 1
            
            while (num_zeros > 1):
                if nums[left_idx] == 0:
                    num_zeros -= 1
                
                left += 1
            
            max_zeros = max(max_zeros, (right_idx - left_idx))
        
        return max_zeros