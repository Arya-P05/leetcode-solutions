class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        max_num_seen = float('-inf')
        count = 0

        for read in range(len(nums)):
            if nums[read] > max_num_seen:
                max_num_seen = nums[read]
                count = 1
                nums[write] = nums[read]
                write += 1
            elif nums[read] == max_num_seen and count < 2:
                count += 1
                nums[write] = nums[read]
                write += 1
        
        return write