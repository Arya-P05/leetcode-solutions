# fuckery how powerful bit manipulation can be when it comes to efficiency

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        
        for idx in range(1, (n + 1)):
            output[idx] = output[idx >> 1] + (idx % 2)
        
        return output
