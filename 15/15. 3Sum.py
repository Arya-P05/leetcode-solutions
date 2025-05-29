from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        arr_len = len(nums)

        for i, number in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = arr_len - 1

            while l < r:
                three_sum = number + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([number, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ans
            