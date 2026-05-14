class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hasht = defaultdict(int)

        # for number in nums:
        #     hasht[number] += 1
        
        # biggest = float('-inf')
        # count = 0

        # for key, val in hasht.items():
        #     if val > count:
        #         count = val
        #         biggest = key
        
        # return biggest

        count = 0
        candidate = 0

        for number in nums:
            if count == 0:
                candidate = number
            
            if number != candidate:
                count -= 1
            else:
                count += 1
        
        return candidate
