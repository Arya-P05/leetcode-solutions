from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # This solution above is O(n) time complexity and O(1) space complexity

        goal = range(len(nums) + 1)

        missing_num = sum(goal) - sum(nums)

        return missing_num

        '''
        First solution (Time: O(n), Space: O(n)):

        new = set()

        for number in range(len(nums)+1):
            new.add(number)
        
        for number in nums:
            new.remove(number)
        
        for result in new:
            return result
        '''
