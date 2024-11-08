# Can't believe I'm uploading this one so late lol

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}

        for idx, number in enumerate(nums):
            pair_val = target - number

            if pair_val in hashm:
                return [hashm[pair_val], idx]
            else:
                hashm[number] = idx
        