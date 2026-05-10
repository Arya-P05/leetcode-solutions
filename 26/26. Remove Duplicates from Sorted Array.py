class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sorted in non decreasing order meaning its either the same or more next index
        write = 0
        last_largest_num_seen = -101

        for read in range(len(nums)):
            if nums[read] > last_largest_num_seen:
                nums[write] = nums[read]
                write += 1
                last_largest_num_seen = nums[read]
        
        return write
