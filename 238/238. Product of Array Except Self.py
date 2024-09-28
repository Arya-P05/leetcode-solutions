from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1

        for idx in range(len(nums)):
            output[idx] = prefix
            prefix *= nums[idx]
        
        suffix = 1

        for idx in range(len(nums) - 1, -1, -1):
            output[idx] *= suffix
            suffix *= nums[idx]
        
        return output
    
def main():
    nums = input("Enter a list of integers separated by spaces: ").strip().split() # turns the input string into a list of strings 
    nums = [int(num) for num in nums] # make the list a list of intergers from list of strings

    solution = Solution()
    result = solution.productExceptSelf(nums)

    print("The product except self array is:", result)

if __name__ == "__main__":
    main()