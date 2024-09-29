from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0

        for idx in range(len(nums)):
            leftSum += nums[idx]

            if leftSum == rightSum:
                return idx
            
            rightSum -= nums[idx]
        
        return -1

def main():
    nums = input("Enter your numbers seperated by a space: ").strip().split()
    nums = [int(num) for num in nums]

    sol = Solution()
    index = sol.pivotIndex(nums)

    print(f"The pivot index is: {index}")

if __name__ == "__main__":
    main()