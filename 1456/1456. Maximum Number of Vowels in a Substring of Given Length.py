class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')

        window_vowel_count = 0
        max_vowel_count = 0

        for idx in range(len(s)):
            if s[idx] in vowels:
                window_vowel_count += 1
            
            if idx >= k and s[idx - k] in vowels:
                window_vowel_count -= 1
            
            max_vowel_count = max(max_vowel_count, window_vowel_count)
        
        return max_vowel_count