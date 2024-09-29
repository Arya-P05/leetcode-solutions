class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        
        while True:
            if word1 == "" and word2 == "":
                break 
            elif word1 != "" and word2 == "":
                new += word1
                word1 = ""
            elif word1 == "" and word2 != "":
                new += word2
                word2 = ""
            else:
                new += word1[0] + word2[0]
                word1 = word1[1:]
                word2 = word2[1:]
        
        return new

def main():
    w1 = input("Enter word 1: ")
    w2 = input("Enter word 2: ")

    merged = Solution()
    new_word = merged.mergeAlternately(w1, w2)
    print(f"Your new word is: {new_word}.")

if __name__ == "__main__":
    main()