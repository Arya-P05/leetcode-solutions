from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def do(asteroids):
            stack = []
            idx = 0

            while (idx < (len(asteroids) - 1)):
                if asteroids[idx] * asteroids[idx + 1] >= 0:
                    stack.append(asteroids[idx])
                elif abs(asteroids[idx]) > abs(asteroids[idx + 1]):
                    stack.append(asteroids[idx])
                    idx += 1
                elif abs(asteroids[idx]) < abs(asteroids[idx + 1]):
                    stack.append(asteroids[idx + 1])
                    idx += 1
                else:
                    idx += 1

                idx += 1
            
            return stack
        
        done = False
        maybe = do(asteroids)
        while(not done):
            for idx in range(len(maybe)-1):
                if idx == len(maybe)-2 and maybe[idx] * maybe[idx+1] > 0:
                    done = True
                elif maybe[idx] * maybe[idx+1] < 0:
                    maybe = do(maybe)
                    break
        
        return maybe
            
            
                

