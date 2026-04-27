import heapq
from collections import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def findMax(nums: List[int]):
        #     maxNum = float("-inf")
        #     maxNumIdx = 0

        #     for idx, number in enumerate(nums):
        #         if number > maxNum:
        #             maxNum = number
        #             maxNumIdx = idx
            
        #     return maxNumIdx

        # res = 0

        # for idx in range(k):
        #     res = nums.pop(findMax(nums))

        # return res
        
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]