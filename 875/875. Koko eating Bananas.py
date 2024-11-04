from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            time = 0

            for pile in piles:
                if mid >= pile:
                    time += 1
                else:
                    time += ceil(pile/mid)
            
            if time > h:
                low = mid + 1
            elif time < h:
                high = mid - 1
            else:
                ans = min(mid, ans)
                high = mid - 1
        
        return ans
    