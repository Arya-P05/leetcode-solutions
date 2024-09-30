from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and char == chars[read]:
                count += 1
                read += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write

def main():
    chars = input("Write your characters seperated by a space: ").strip().split()
    compressed = Solution()
    length = compressed.compress(chars)
    print(f"The length of the compressed characters is: {length}")

if __name__ == "__main__":
    main()