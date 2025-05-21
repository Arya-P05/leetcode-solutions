from collections import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        subsequence = []
        subsequence.append(words[0])

        last_group = groups[0]

        for idx in range(1, len(words)):
            if groups[idx] != last_group:
                last_group = groups[idx]
                subsequence.append(words[idx])
        
        return subsequence
    