from collections import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_out_row_zero = False

        row_len = len(matrix)
        col_len = len(matrix[0])

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row == 0:
                        zero_out_row_zero = True
                    else:
                        matrix[row][0] = 0

        for row in range(1, row_len):
            for col in range(1, col_len):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(row_len):
                matrix[row][0] = 0

        if zero_out_row_zero == True:
            for col in range(col_len):
                matrix[0][col] = 0
                