from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # if its an odd number of negative numbers, one of them will have to be
        # negative at the end, so make that the smallest negative.

        # if its an even number of negative numbers, we can turn all of them positive

        positives = []
        negatives = []
        zeros = []
        lowest = float("inf")

        for row in matrix:
            for num in row:
                if num < 0:
                    negatives.append(num)
                elif num > 0:
                    positives.append(num)
                else:
                    zeros.append(num)
            
                if abs(num) < lowest:
                    lowest = abs(num)
        
        total = 0

        if len(negatives) % 2 == 0:
            total = sum(positives) + (-sum(negatives))
        elif len(zeros) > 0:
            total = sum(positives) + (-sum(negatives))
        else:
            total = sum(positives) + (-sum(negatives)) + (-lowest * 2)
        
        return total
