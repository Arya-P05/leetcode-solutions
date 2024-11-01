class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        tempWord = ""

        for letter in s:
            if letter != " ":
                tempWord += letter
            elif tempWord != "":
                output.append(tempWord)
                tempWord = ""
        
        if tempWord != "":
            output.append(tempWord)
            tempWord = ""
        
        return " ".join(output[::-1])
