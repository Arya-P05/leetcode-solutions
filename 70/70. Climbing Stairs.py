class Solution:
    def climbStairs(self, n: int) -> int:
        # so at each step you can do 1 or 2 until you hit max 
        # last step has to take you to n not more 
        # do you do recursion?
            # like start with 1 step and then do either 1 or 2 and repeat for all of them and count the valid ones
            # and also start with 2 step and then repeat like above
        
        # def take_one_step(curr_level):
        #     return curr_level + 1
        
        # def take_two_step(curr_level):
        #     return curr_level + 2

        # res = 0
        # curr_level = 0

        # while curr_level <= n:
        #     if curr_level == n:
        #         res += 1
        #         break
        #     else:

        # nvm i watched neetcode and learned what DP was lol

        one = 1
        two = 1

        for idx in range(n - 1):
            temp = one
            one += two
            two = temp
        
        return one

        
