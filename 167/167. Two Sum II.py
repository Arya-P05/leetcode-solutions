from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr_len = len(numbers)
        max_possible = arr_len - 1
        idx = 0
        
        while True:
            if numbers[idx] + numbers[max_possible] > target:
                max_possible -= 1
                continue
            elif numbers[idx] + numbers[max_possible] < target:
                idx += 1
                continue
            else:
                return [idx + 1, max_possible + 1]

        return 0
    