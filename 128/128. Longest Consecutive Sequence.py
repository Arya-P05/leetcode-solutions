from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for number in numbers:
            if number - 1 not in numbers:
                curr = number
                streak = 1

                while curr + 1 in numbers:
                    streak += 1
                    curr += 1
                
                longest = max(streak, longest)
        
        return longest
            