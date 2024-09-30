from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashm = {}

        for num in arr:
            if num in hashm:
                hashm[num] += 1
            else:
                hashm[num] = 1

        return len(set(hashm.values())) == len(hashm.values())

def main():
    nums = input("Write your numbers seperated by a space: ").strip().split()
    nums = [int(num) for num in nums]

    unique = Solution()
    unique = unique.uniqueOccurrences(nums)
    
    if unique:
        print("Your inputted numbers did infact have a unique number of occurrences!")
    else:
        print("Your inputted numbers did NOT have a unique number of occurrences!")

if __name__ == "__main__":
    main()