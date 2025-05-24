from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        
        for idx in range(len(words)):
            if x in words[idx]:
                output.append(idx)

        return output
