from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
            
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
    
def main():
    str1 = input("String 1: ")
    str2 = input("String 2: ")

    common = Solution()
    common = common.gcdOfStrings(str1, str2)

    print(f"The common string between the two is: {common}")

if __name__ == "__main__":
    main()