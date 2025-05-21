from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        curr_row = set()
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for row_idx in range(9):
            for col_idx in range(9):
                curr_cell = board[row_idx][col_idx]

                if curr_cell == '.':
                    continue

                if curr_cell in curr_row or curr_cell in sub_boxes[(row_idx//3, col_idx//3)] or curr_cell in cols[col_idx]:
                    return False
                else:
                    curr_row.add(curr_cell)
                    sub_boxes[(row_idx//3, col_idx//3)].add(curr_cell)
                    cols[col_idx].add(curr_cell)

            curr_row = set()
        
        return True
                   
        