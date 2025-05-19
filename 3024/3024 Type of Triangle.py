from collections import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        side_one = nums[0]
        side_two = nums[1]
        side_three = nums[2]

        if side_one + side_two > side_three and side_one + side_three > side_two and side_three + side_two > side_one:
            if side_one == side_two == side_three:
                return "equilateral"
            elif side_one == side_two or side_two == side_three or side_one == side_three:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"