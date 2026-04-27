import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # everything has 2 divisors by default (1 and the number itself) so we just need to check for exactly 2 more
        # then add up all the divisors 
        
        ans = 0

        for number in nums:
            increasing_num = 2
            divisors = [1, number]

            while increasing_num <= math.sqrt(number):
                if len(divisors) > 4:
                    break

                if number % increasing_num == 0:
                    divisors.append(increasing_num)

                    if (number // increasing_num != increasing_num):
                        divisors.append(number // increasing_num)
                
                increasing_num += 1

            if len(divisors) == 4:
                ans += divisors[0] + divisors[1] + divisors[2] + divisors[3]

        return ans
        