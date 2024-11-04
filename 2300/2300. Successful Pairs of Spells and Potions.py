from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # successful if spells[i] * potions[j] >= success

        output = []

        potions.sort()
        potions_count = len(potions) - 1

        for spell in spells:
            low = 0
            high = potions_count
            valid_idx = potions_count
            
            while low <= high:
                mid = (low + high) // 2

                if spell * potions[mid] >= success:
                    valid_idx = mid - 1
                    high = mid - 1
                else:
                    low = mid + 1
            
            output.append(potions_count - valid_idx)
        
        return output
