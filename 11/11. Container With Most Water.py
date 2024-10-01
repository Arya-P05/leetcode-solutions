from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left = 0
        right = len(height) - 1

        while left <= right:
            left_height = height[left]
            right_height = height[right]

            if left_height <= right_height:
                area = left_height * (right - left)
                left += 1
            else:
                area = right_height * (right - left)
                right -= 1
            
            if area > maxA:
                maxA = area
        
        return maxA  

def main():
    heights = input("Write the height of each line seperated by a space: ").strip().split()
    heights = [int(num) for num in heights]

    area = Solution()
    area = area.maxArea(heights)

    print(f"The max area we can have is: {area}")

if __name__ == "__main__":
    main()