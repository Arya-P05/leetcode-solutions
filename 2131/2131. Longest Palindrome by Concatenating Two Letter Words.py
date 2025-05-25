from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # have to remember how many times palindrome pairs came and if they appear in pairs of 2 then we can add 4 to the count and one time add a single pair to go in the middle
        # count the number of times non-palindrome ones showed up and the min(forward, backward) is what we add to the count

        word_count = Counter(words)
        ans = 0
        middle_added = False

        for string in list(word_count.keys()):
            cnt = word_count[string]

            if string[0] == string[1]:
                pairs = cnt // 2
                ans += 4 * pairs
                
                if cnt % 2 == 1 and not middle_added:
                    ans += 2
                    middle_added = True
            else:
                rev = string[::-1]
                pairs = min(cnt, word_count.get(rev, 0))
                if pairs != 0:
                    ans += pairs * 4
                    word_count[string] -= pairs
                    word_count[rev] -= pairs
        
        return ans
