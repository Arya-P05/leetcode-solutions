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
    
def main():
    s = str(input("What sentence do you want to reverse? "))
    sol = Solution()
    sol = sol.reverseWords(s)
    print(f"The reversed string is: {sol}")

if __name__ == "__main__":
    main()
