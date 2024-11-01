from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length_set = len(set(nums))
        length_nums = len(nums)

        return length_nums != length_set