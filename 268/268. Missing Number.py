from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new = set()

        for number in range(len(nums)+1):
            new.add(number)
        
        for number in nums:
            new.remove(number)
        
        for result in new:
            return result
