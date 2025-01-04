# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        max_number = n
        min_number = 1

        while min_number <= max_number:
            my_guess = (max_number + min_number) // 2
            result = guess(my_guess)

            if result < 0:
                max_number = my_guess - 1
            elif result > 0:
                min_number = my_guess + 1
            else:
                return my_guess