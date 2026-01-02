from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for idx in range(len(nums) - 2):
            if nums[idx] == nums[idx + 1] or nums[idx] == nums[idx + 2]:
                return nums[idx]
        
        return nums[-1]
        