from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                if digit == ".":
                    continue
                
                if digit in rows[row] or digit in cols[col] or digit in squares[row // 3, col // 3]:
                    return False
                else:
                    rows[row].add(digit)
                    cols[col].add(digit)
                    squares[row // 3, col // 3].add(digit)

        return True
                   
        