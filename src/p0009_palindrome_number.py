# 9. Palindrome Number
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Example 1: Input: x = 121 Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2: Input: x = -121 Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3: Input: x = 10 Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Constraints: -231 <= x <= 231 - 1
# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    # without string conversion
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        mirror = 0
        original = x
        while x > 0:
            mirror = mirror * 10 + x % 10
            x //= 10
        return mirror == original

    # first idea, not so fast :) without strings
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        int_len = 0
        x_temp = x
        while x_temp > 0:
            int_len += 1
            x_temp //= 10
        
        while int_len > 1:
            # print(x, "|", x // pow(10,int_len-1), x % pow(10,int_len-1) // 10, x % 10)
            if x // pow(10,int_len-1) != x % 10:
                return False
            x = x % pow(10,int_len-1) // 10
            int_len -= 2

        return True

sol = Solution()
print(sol.isPalindrome(123456789))
print(sol.isPalindrome(123454321))
print(sol.isPalindrome(12344321))

x = 12345678
print(x, "|", x // pow(10,7), x % 10, "|", x % pow(10,7) // 10)