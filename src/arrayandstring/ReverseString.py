# 334. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1: Input: s = ["h","e","l","l","o"] Output: ["o","l","l","e","h"]
# Example 2: Input: s = ["H","a","n","n","a","h"] Output: ["h","a","n","n","a","H"]
# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left_pointer = 0
        rigth_pointer = len(s)-1
        while left_pointer < rigth_pointer:
            s[left_pointer], s[rigth_pointer] = s[left_pointer], s[rigth_pointer]
            left_pointer += 1
            rigth_pointer -=1


if __name__ == "__main__":
    somelist = list(["h","e","l","l","o"])
    sol = Solution()
    sol.reverseString(somelist)
    print(somelist)
