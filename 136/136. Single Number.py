from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for number in nums:
            xor ^= number
        
        return xor