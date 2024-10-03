from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        left = 0
        right = len(nums) - 1

        while(left < right):
            sum = nums[left] + nums[right]

            if sum == k:
                left += 1
                right -= 1
                count += 1
            elif sum > k:
                right -= 1
            elif sum < k:
                left += 1
        
        return count

def main():
    nums = input("Enter numbers seperated by a space: ").strip().split()
    nums = [int(num) for num in nums]

    k = int(input("What is the target number: "))

    num_of_max_operations = Solution()
    num_of_max_operations = num_of_max_operations.maxOperations(nums, k)
    print(f"The number of max operations we could do on your list of numbers is: {num_of_max_operations}")

if __name__ == "__main__":
    main()

                
