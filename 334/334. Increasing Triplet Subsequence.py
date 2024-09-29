from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        f, s = float("inf"), float("inf")

        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            else: 
                return True

        return False

def main():
    nums = input("Type in your numbers seperated by a space: ").strip().split()
    nums = [int(num) for num in nums]
    value = Solution()
    thing = value.increasingTriplet(nums)
    print(f"Your inputted numbers have an increasing triplet subsequence: {thing}")

if __name__ == "__main__":
    main()
