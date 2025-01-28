from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            count = [0] * 26    

            for char in word:
                count[ord(char) - ord('a')] += 1

            organized_wrd = ''.join(chr(idx + ord('a')) * count[idx] for idx in range(26))
            
            if organized_wrd in words:
                words[organized_wrd].append(word)
            else:
                words[organized_wrd] = [word]
            
        return words.values()
    