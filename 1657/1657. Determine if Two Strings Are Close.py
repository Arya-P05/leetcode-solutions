class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        letters1 = [0] * 26
        letters2 = [0] * 26

        for letter in word1:
            letters1[ord(letter) - ord('a')] += 1
        
        for letter in word2:
            letters2[ord(letter) - ord('a')] += 1
        
        for idx in range(26):
            if letters1[idx] == 0 and letters2[idx] != 0:
                return False
            elif letters2[idx] == 0 and letters1[idx] != 0:
                return False
        
        letters1.sort()
        letters2.sort()

        return letters1 == letters2