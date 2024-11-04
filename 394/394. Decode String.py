class Solution:
    def decodeString(self, s: str) -> str:
        # add to stack until you face a "]"
        # then you add to a temp string until you get to "["
        # then you get the amount of times it repeats by checking if its a digit
        # add the temp string times the number you get to the stack end
