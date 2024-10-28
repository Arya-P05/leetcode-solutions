from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return 0
        elif length == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        else:
            for idx in range(length):
                if idx == 0:
                    if nums[idx] > nums[idx+1]:
                        return idx
                elif idx == length - 1:
                    if nums[idx-1] < nums[idx]:
                        return idx
                elif nums[idx-1] < nums[idx] and nums[idx] > nums[idx+1]:
                    return idx
            