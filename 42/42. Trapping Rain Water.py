from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [0] * len(height)
        max_left = 0
        max_rights = [0] * len(height)
        max_right = 0

        for idx in range(len(height)):
            if idx == 0:
                continue
            else:
                max_left = max(max_left, height[idx-1])
                max_lefts[idx] = max_left
        
        for idx in range(len(height)-1, -1, -1):
            if idx == (len(height) - 1):
                continue
            else:
                max_right = max(max_right, height[idx+1])
                max_rights[idx] = max_right

        max_area = 0

        for idx in range(len(height)):
            if (min(max_rights[idx], max_lefts[idx]) - height[idx]) > 0:
                max_area += min(max_rights[idx], max_lefts[idx]) - height[idx]

        return max_area
    