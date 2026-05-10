class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # because its in place the whole point is to have 2 pointers where you have one at the index that you will do something to once you find another suitable index using the other pointer

        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        
        return write