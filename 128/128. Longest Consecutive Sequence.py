from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = sorted(set(nums)) # is O(nlog(n)) because of sorted
        longest = [1] * len(nums)
        index = 0

        for idx in range(len(numbers)-1):
            if numbers[idx] + 1 == numbers[idx+1]:
                longest[index] += 1
            else:
                index += 1
        
        biggest = 0

        for number in longest:
            if number > biggest:
                biggest = number
        
        return biggest
            