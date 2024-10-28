from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = None
        count = 0

        for number in nums:
            if count == 0:
                winner = number
            
            if number == winner:
                count += 1
            else:
                count -= 1
            
        return winner