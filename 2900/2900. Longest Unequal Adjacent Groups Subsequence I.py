from collections import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        arr_len = len(words)
        longest_sequence = [words[0]]
        longest_sequence_count = 1
        previous_group = groups[0]

        for idx in range(1, arr_len):
            if groups[idx] == previous_group:
                continue
            else:
                previous_group = groups[idx]
                longest_sequence_count += 1
                longest_sequence.append(words[idx])
        
        return longest_sequence
    