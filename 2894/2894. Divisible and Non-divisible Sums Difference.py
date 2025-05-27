class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for number in range(1, n+1):
            if number % m != 0:
                num1 += number
            else:
                num2 += number

        return num1 - num2
    