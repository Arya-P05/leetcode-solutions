class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        vowels = ('a', 'e', 'i', 'o', 'u')
        left = 0
        max_count = 0

        for letter in s[0:k]:
            if letter in vowels:
                max_count += 1

        curr = max_count

        for right_idx, letter in enumerate(s):
            if right_idx >= k:
                if s[left] in vowels and letter not in vowels:
                    curr -= 1
                elif s[left] not in vowels and letter in vowels:
                    curr += 1
                left += 1
                max_count = max(max_count, curr)
        
        return max_count