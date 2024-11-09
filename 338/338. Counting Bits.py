# my solution without knowing bit manipulation or anything about bits lol
# also very surprising that this passes without timing out because its quite inefficient

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        
        for idx in range(len(output)):
            binary_rep = str(bin(idx))

            for number in binary_rep:
                if number == '1':
                    output[idx] += 1
        
        return output
