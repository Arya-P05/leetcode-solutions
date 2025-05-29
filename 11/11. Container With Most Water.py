from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)

            if curr_area >= max_area:
                max_area = curr_area
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return max_area

def main():
    heights = input("Write the height of each line seperated by a space: ").strip().split()
    heights = [int(num) for num in heights]

    area = Solution()
    area = area.maxArea(heights)

    print(f"The max area we can have is: {area}")

if __name__ == "__main__":
    main()