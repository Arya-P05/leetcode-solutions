from typing import List
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for word in strs:
            count = [0] * 26    

            for char in word:
                count[ord(char) - ord('a')] += 1

            key_wrd = tuple(count)

            words[key_wrd].append(word)
            
        return words.values()
    