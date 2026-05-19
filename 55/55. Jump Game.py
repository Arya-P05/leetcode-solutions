class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # this seems like a back tracking problem kinda but not exactly lol
        # so start from second last idx and mark true if you can get to end, then move back and mark true if you can get to any of the idxs marked as true ahead of it

        num_status = [False] * len(nums)
        num_status[-1] = True

        for idx in range(len(nums) - 1, -1, -1):
            farthest = min(idx + nums[idx], len(nums) - 1)

            for index in range(idx + 1, farthest + 1):
                if num_status[index]:
                    num_status[idx] = True
                    break
        
        return num_status[0]
                




                 