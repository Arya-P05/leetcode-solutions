class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for idx in range(len(s)):
            if s[idx] != "*":
                stack.append(s[idx])
            else:
                stack.pop()
        
        return "".join(stack)
    