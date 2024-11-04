from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = ceil(sum(piles) / h)
        high = max(piles)
        ans = high

        while low < high:
            mid = (low + high) // 2
            time = 0

            for pile in piles:
                    time += ceil(pile/mid)
            
            if time > h:
                low = mid + 1
            else:
                ans = min(mid, ans)
                high = mid
        
        return ans
    