class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # for the first and last row the next letter is (numRows - 1) * 2 
        # distance away in the string

        # for the rows in between the first and last row the letters are
        # (numRows - 1) * 2 - (2 * curr_row)
        # with curr_row starting from 0

        if numRows == 1:
            return s
        
        increment = (numRows - 1) * 2 
        ans = ""
        
        for row in range(numRows):
            for idx in range(row, len(s), increment):
                ans += s[idx]

                if (row > 0) and (row < numRows - 1) and (idx + increment - 2 * row < len(s)):
                    ans += s[idx + increment - 2 * row]

        return ans